import os
import string

from shrota.models import Signs

from .read_single_frames import get_handpoints_from_singleframe


def run():
    """
    Function to fetch x,y,z handpoint coordinates for every frame and load into db
    :return:
    """
    ip = None
    try:
        Signs.objects.all().delete()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dataset_path = os.path.join(dir_path, "alphabet_dataset\\")
        print("Confirm dataset path:", dataset_path)
        dataset_names = list(string.ascii_lowercase)
        for i in dataset_names:
            image_path = (dataset_path + i + ".png")
            res = get_handpoints_from_singleframe(image_path)
            ip = i
            x = res[0]
            y = res[1]
            z = res[2]
            sign = Signs(gesture=str.upper(i),
                         x0=x[0],
                         x1=x[1],
                         x2=x[2],
                         x3=x[3],
                         x4=x[0],
                         x5=x[0],
                         x6=x[0],
                         x7=x[7],
                         x8=x[8],
                         x9=x[9],
                         x10=x[10],
                         x11=x[11],
                         x12=x[12],
                         x13=x[13],
                         x14=x[14],
                         x15=x[15],
                         x16=x[16],
                         x17=x[17],
                         x18=x[18],
                         x19=x[19],
                         x20=x[20],
                         y0=y[0],
                         y1=y[1],
                         y2=y[2],
                         y3=y[3],
                         y4=y[0],
                         y5=y[0],
                         y6=y[0],
                         y7=y[7],
                         y8=y[8],
                         y9=y[9],
                         y10=y[10],
                         y11=y[11],
                         y12=y[12],
                         y13=y[13],
                         y14=y[14],
                         y15=y[15],
                         y16=y[16],
                         y17=y[17],
                         y18=y[18],
                         y19=y[19],
                         y20=y[20],
                         z0=z[0],
                         z1=z[1],
                         z2=z[2],
                         z3=z[3],
                         z4=z[0],
                         z5=z[0],
                         z6=z[0],
                         z7=z[7],
                         z8=z[8],
                         z9=z[9],
                         z10=z[10],
                         z11=z[11],
                         z12=z[12],
                         z13=z[13],
                         z14=z[14],
                         z15=z[15],
                         z16=z[16],
                         z17=z[17],
                         z18=z[18],
                         z19=z[19],
                         z20=z[20])

            sign.save()
            print(i, 'loaded to DB!')
    except Exception as e:
        print('Failed at i:', ip)

