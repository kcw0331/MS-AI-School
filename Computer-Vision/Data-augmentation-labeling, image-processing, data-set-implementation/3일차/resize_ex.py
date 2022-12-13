from PIL import Image

def expand2square(pil_img, background_color): # 백그라운드 컬러를 검정색으로해준다.
    width, height = pil_img.size
    # print(width, height)
    if width == height: # 정사각형이라면 리사이즈 해도 필요가 없다.
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        # image add (추가 이미지 , 붙일 위치 (가로 , 세로))
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

img = Image.open("./imges.png")
img_new = expand2square(img, (0, 0, 0)).resize((224, 224)) # 데이터의 크기를 224로 맞추었다.
img_new.save("./test.png") # pil에서는 save로 저장을 해준다.
# <PIL.JpegImagePlugin.JpegImageFile 
# image mode=RGB size=174x290 at 0x215AC652320>