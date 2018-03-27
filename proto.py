from PIL import Image

# start = len(pixelmap[0,0])-3
# temp_map = pixelmap[i,j][start:]
# process rgb value~
# pixelmap[i,j] = pixelmap[i,j][::-1][3:] + temp_map # save it!


def inversion(img):
    pixelmap = img.load()
    start = len(pixelmap[0,0])-3
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            temp = pixelmap[i,j][start:]
            temp = (temp[0] & 0xFF, temp[1] ^ 0xFF, temp[2] ^ 0xFF)
            pixelmap[i,j] = pixelmap[i,j][::-1][3:] + temp
        return img

def rgb_plain(img, mask=(0,0,0)):
    pixelmap = img.load()
    start = len(pixelmap[0,0])-3
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            temp = pixelmap[i,j][start:]
            temp[i,j] = (temp[0] & mask[0], temp[1] & mask[1], temp[2] & mask[2])
            pixelmap[i,j] = pixelmap[i,j][::-1][3:] + temp
        return img

def bit_set(img, param=0x000000): # input param in hex code
    pixelmap = img.load()
    start = len(pixelmap[0,0])-3
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                temp = pixelmap[i,j][start:]
                # do something for it!
                pixelmap[i,j] = pixelmap[i,j][::-1][3:] + temp
        return img
