# train loop
# val loop
# 모델 save
# 평가 함수

import torch
import os
import torch.nn as nn # nn은 모델의 아키텍쳐를 만들때 사용한다.

# 모델에서 나온 값이 output이고 test값은 target이다.
def calculate_acc(output, target):
    # 평가 함수
    output = torch.signoid(output) >= 0.5 # 0.5이상인 애들을 넣어준다.
    target = target == 1.0
    return torch.true_divide((output == target).sum(dim=0), output.size(0)).item()
    # 두개가 동일하게 되었을 때, 

def save_model(model, save_dir, file_name = "last.pt"):
    # save model
    os.makedirs(save_dir, exist_ok=True)
    output_path = os.path.join(save_dir, file_name)
    if isinstance(model, nn.DataParallel): # 분산처리로 되면 따로 저장이 된다.
        print("멀티 GPU 저장 !!") # 실무에서는 멀티 GPU을 사용하기 때문에 if문을 만들어 주었다.
        torch.save(model.module.state_dict()) # 모델의 상태정보를 저장해준다.
    else:
        print("싱글 GPU 저장 !!")
        torch.save(model.state_dict(), output_path) # 싱글이라서 모델의 상태를 바로 저장한다.