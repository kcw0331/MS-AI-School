from PIL import Image
import os

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

def image_file(image_folder_path):
    all_root = []
    # print(",,", xml_folder_path)
    for (path, dir, files) in os.walk(image_folder_path): # walk로 하게 되면, path, dir, files로 읽어온다.
        # print("...", path, dir, files)
        for filename in files:
            # image.png -> .png 이렇게 나오게 된다.
            # image.xml -> .xml
            ext = os.path.splitext(filename)[-1]
            # print(filename)
            if ext == ".jpg":
                root = os.path.join(path, filename)
                # ./cavt_annotations/annotations.xml
                all_root.append(root) # 여기에 저장을 해준다.
            else:
                print("no xml file..")
                break # 이렇게 해야 all root를 빠져 나가게 된다.
    return all_root

img_path_list = image_file("./images/")
# print(image_path_list)
# ['./images/kiwi_1.jpg', './images/kiwi_2.jpg', './images/kiwi_3.jpg', './images/kiwi_4.jpg', './images/kiwi_5.jpg', './images/kiwi_6.jpg', './images/kiwi_7.jpg']

for img_path in img_path_list:
    # print(img_path)
    # image_name_temp = img_path.split("/") # 쪼개진걸로 해서 이미지를 가져온다. 
    image_name_temp = os.path.basename(img_path) # 파일명만 가지고 온 다음
    """image_name_temp2 = os.path.abspath(img_path)
    print(image_name_temp2) # 상대 경로를 가지고 온다."""
    image_name = image_name_temp.replace(".jpg", "")  # .jpg를 날려준다. # 파일이름을 뽑아냄
    # print(image_name_temp)

    img = Image.open(img_path)
    img_new = expand2square(img, (0, 0, 0)).resize((224, 224)) # 데이터의 크기를 224로 맞추었다.
    os.makedirs("./resize", exist_ok = True) # resize라는 파일을 만들어 준다. 파일이 존재하면 만들지 않는다.
    img_new.save(f"./resize/{image_name}.png", quality = 100)

