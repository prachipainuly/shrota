import { Camera } from '@mediapipe/camera_utils';
import { drawConnectors, drawLandmarks } from '@mediapipe/drawing_utils';
import { Hands, HAND_CONNECTIONS } from '@mediapipe/hands';
import React, { useEffect, useRef, useState } from 'react'
import Webcam from 'react-webcam';
import { api } from '../api';
import { useGameContext, useUpdateGame } from '../contexts/GameContext';

const MPHands = () => {
  const webcamRef = useRef(null)
  const canvasRef = useRef(null)
  const gameContext = useGameContext()
  const updateGameContext = useUpdateGame()
  const [ frameResults, setFrameResults ] = useState()
  const [ results, setResults ] = useState()

  useEffect(() => {
    const hands = new Hands({
      locateFile: (file) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/hands@0.4.1646424915/${file}`;
      },
    });
    hands.setOptions({
      maxNumHands: 2,
      minDetectionConfidence: 0.5,
      minTrackingConfidence: 0.5,
      modelComplexity: 1,
    });
    hands.onResults(onResults);

    if (
      typeof webcamRef.current !== "undefined" &&
      webcamRef.current !== null
    ) {
      const camera = new Camera(webcamRef.current.video, {
        onFrame: async () => {
          await hands.send({ image: webcamRef.current.video });
        },
        width: '70vh',
        height: '50vh',
      });
      camera.start()
    }
  }, []);

  useEffect(() => {
    if(gameContext.sendFrame === true && results){
      console.log("send frame true")
      updateGameContext({...gameContext, scoreLoading: true})
      const reqBody = {
        right_handpoints: results, 
        word: gameContext.words[gameContext.currentWord]
      }
      api.post("/calculate_round_result/", reqBody).then(
        res => {
          res.data.result.includes('error') ?
            updateGameContext({...gameContext, bottomText: "No hands detected!", scoreLoading: false, showScore: true})
          :
            updateGameContext({...gameContext, bottomText: `Result of the last symbol: ${res.data.result}`, scoreLoading: false, showScore: true})
        }
      ).catch(function(error) {
          updateGameContext({...gameContext, bottomText: `Error obtaining your results.`, scoreLoading: false, showScore: true})
      }).finally(() => {
        setResults()
      })
    } 

    if(gameContext.catchFrame && !results){
      console.log("catchFrame true")
      let x = []
      let y = []
      let z = []
      frameResults.multiHandLandmarks.map(hand => {
        hand.map(landmarks => {
          x.push(landmarks.x)
          y.push(landmarks.y)
          z.push(landmarks.z)
        })})

      setResults({x, y, z})
    }
  }, [gameContext.sendFrame, gameContext.catchFrame])

  const onResults = (results) => {
    if(results){
      setFrameResults(results);
    }

    const videoWidth = webcamRef.current.video.videoWidth;
    const videoHeight = webcamRef.current.video.videoHeight;
    canvasRef.current.width = videoWidth;
    canvasRef.current.height = videoHeight;
    const canvasElement = canvasRef.current;
    const canvasCtx = canvasElement.getContext("2d");
    canvasCtx.save();
    canvasCtx.clearRect(0, 0, videoWidth, videoHeight);
    canvasCtx.translate(videoWidth, 0);
    canvasCtx.scale(-1, 1);
    canvasCtx.drawImage(
      results.image,
      0,
      0,
      canvasElement.width,
      canvasElement.height
    );
    if (results.multiHandLandmarks) {
      
      for (const landmarks of results.multiHandLandmarks) {
        drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS, {
          color: "#00FF00",
          lineWidth: 5,
        });
        drawLandmarks(canvasCtx, landmarks, { color: "#FFFFFF", lineWidth: 2 });
      }
    }
    canvasCtx.restore();
    
  };

  return (
    <div>
      <Webcam
        audio={false}
        mirrored={true}
        ref={webcamRef}
        style={{
          position: "absolute",
          marginLeft: "auto",
          marginRight: "auto",
          textAlign: "center",
          zindex: 9,
          width: '70vh',
          height: '50vh',
        }}
      />
      <canvas
        ref={canvasRef}
        style={{
          position: "absolute",
          marginLeft: "auto",
          marginRight: "auto",
          textAlign: "center",
          zindex: 9,
          width: '70vh',
          height: '50vh',
        }}
      ></canvas>
    </div>
  );
};

export default MPHands