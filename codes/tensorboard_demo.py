# Tensorboard 的使用

from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")

image_path = r"hymenoptera_data_2\train\bees_image\16838648_415acd9e3f.jpg"
image_PIL = Image.open(image_path)
image_array = np.array(image_PIL) # 直接将PIL类型的图片转换成np.array类型，符合add_image输入要求

# 添加一个图像数据到summary中，dataformats表示np.array的形状，默认CHW，C是通道数3
writer.add_image("test_image", image_array, 2, dataformats="HWC")

# 画 y = 2x
for i in range(100):
    writer.add_scalar("y=3x", 3*i, i) # 添加一个标量数据（scalar data）到summary中，画图

writer.close() # 将log写完之后，记得close()

# 以下为REPL调试，逐行运行
# image_path = r"hymenoptera_data_2\train\ants_image\0013035.jpg"
# import numpy as np
# from PIL import Image
# image = Image.open(image_path)
# type(image)
# image_array = np.array(image) # 直接将PIL类型的图片转换成np.array类型，符合add_image输入要求
# image_array.shape # 发现是（H，W，C）形状的，不是默认的CHW
