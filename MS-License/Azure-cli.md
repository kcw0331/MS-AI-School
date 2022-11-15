# Azure Cli, Docker와 쿠버네티스 
* 2022년 11월 15일(화) - DP-900에 대해 설명하시면서 Azure Portal에서 실습을 해주심.
* 첫번째, Azure cli를 사용해서 계정을 만드는 것과 삭제하는 것을 진행함.
*  두번째, Auzre cli를 사용해서 ACR에 도커를 만들고 쿠버네티스로 배포하려는 것까지 진행을 함.

### 1. Azure portal에서 Windows 11가상머신을 만들고 가상환경에서 Azure cli를 실행해본다.

1) azure의 cli가 잘 설치 되었나 확인을 해본다. 
    ```
    > az 
    ```

2) 로그인을 하게 되면, 윈도우 웹에서 마이크로소프트로 로그인 하라는 창이 나오게 된다.
    ```
    > az login 
    ```
3) az list를 하게 되면, az cli안에 어떤 것이 있는지 확인을 해 볼 수 있다.
    ```
    > az list 
    ```
4) az account list를 하게 되면 권한이 충분하지 않아서 자기꺼만 나오게 된다.
    ```
    > az account list 
    ```
5) vm안에 어떠한게 있는지 확인해 보기 위해 az vm list를 쳐서 확인해 볼 수 있다.
    ```
    > az vm list 
    ```
6) 그룹 리스트 안에 어떠한게 있는지 확인해 볼 수 있다.
    ```
    > az group list 
    ```
7) 그룹을 RGTest2로 생성을 한다. 그 후 지역을 eastus로 설정을 하고 애저 포탈에 RGTest2가 성성이 되어 있는지 확인해 볼 수 있다.
    ```
    > az group create --name RGTest2 --location eastus 
    ```
8) 가상 네트워크(vnet)를 만들었다. vnet을 생성해주고, 리소스 그룹을 RGTest2로 지정해준다. 그리고 vnet과 subnet을 지정해준다. 그 다음 vnet의 prefixes와 subnet의 prefixes를 지정해 준다.
    ```
    > az network vnet create --name labuser2vnet --resource-group RGTest2 --subnet-name labuser2subnet --address-prefixes 10.0.0.0/16 --subnet-prefixes 10.0.0.0/24 
    ```
9) 가상 머신을 만든다.(어떤 가상머신 이미지를 사용할지 중요하다.!!!)
- 이미지를 선택하고 버전을 생략하게 되면 최신버전을 설치해주게 된다. vnet과 subnet을 지정해준다. subnet은 -name을 지정해주지 않아도 된다. azure cli상에서는 작업이 시작되면 Running이라는 표시가 나오게 된다. --generate-ssh-keys는 키를 만들면서 실행을 시켜주는 것이다. 그 후 나중에는 keys파일로 인증을 해주게 된다.
    ```
    > az vm create --resource-group RGTest2 --name labuser2testvm --image UbuntuLTS --vnet-name labuser2vnet --subnet labuser2subnet --generate-ssh-keys 
    ```
**그래서 스크립트 기반으로 해서 가상머신을 만드는 것을 해보았다.**

**-- 이거는 네임이고 - 하나는 이름을 뜻한다.**

---

1)  어떤 것이 생성되었는지를 본다. show는 이 안에 무엇을 보여줄지 써줘야 한다. 그런데 이렇게 적어주게 되면 오류가 나게 된다.
    ```
    > az vm show --name labuser2testvm 
    ```
11) 그리고 또 이렇게 적어주게 되도 오류가 나게 된다.
    ```
    > az vm show --name labuser2testvm -resource-group RGTest2 
    ```
12) 이렇게 적어주게 되면, 오류는 나지 않게 된다고 하였으나 무언가 오류가 나게 되었다.
    ```
    > az vm show --name labuser2testvm --resource-group RGTest2 --query 'networkProfile.networkInterfacees[].id' 
    ```
13) 삭제를 할 때는 아래와 같이 삭제를 코드를 작성하게 되면 삭제가 이루어지게 된다.
    ```
    > az group delete --name RGTest2 #
    ```

---

### 2. DP-900에서 PowerBI에 대해 설명을 해주신 다음에 다시 Azure cli를 사용해서 실습을 해본다.

1) acr은 애저 컨테이너 레지스트리를 만드는 것이다. 이걸 실행하게 되면, 바로 acr을 실행이 된다.
    ```
    > az acr create --resource-group RG2 --name labuser2acr --sku Basic 
    ```
2) AKS를 만드는 것을 해본다.(애저 쿠버네티스 서비스를 생성해본다.) 
    ```
    > # az aks create --resource-group MyResourceGroup --name MyAKS --location eastus --attach-acr MyHelmACR --generate-ssh-keys
    > az aks create --resource-group RG2 --name labuser2aks --location eastus --attach-acr labuser2acr --generate-ssh-keys # <- 키방식으로 입력되는데, 키가 자동으로 생성되게 만들어 준다.
    ```

---

### 3. 쿠베시티엘을 설치한다.

3) 애저 쿠버네티스 서비스에 cli를 설치해준다.
    ```
    > az aks install-cli 
    ```
4) 접속에 필요한 인증을 만들어 준다.
    ```
    > # az aks get-credentials --resource-group MyResourceGroup --name MyAKS # <- 접속에 필요한 인증을 만든다.
    > az aks get-credentials --resource-group RG2 --name labuser2aks
    ```
5) 깃이 가상환경에 설치가 되어있지 않아서 Git을 사이트에서 설치를 해준다. 그 다음 클론을 사용해서 다운을 받아준다.
    ```
    > # https://github.com/Azure-Samples/azure-voting-app-redis.git # <- 여기에 있는 것을 클론하였다.
    > git clone https://github.com/Azure-Samples/azure-voting-app-redis.git
    ```
6) azure-voting-app-redis 디렉토리로 이동해준다.
    ```
    > cd azure-voting-app-redis
    ```
7) windows에서는 dir를 치게 되면, 현재 파일에 무엇이 있는지를 볼 수 있다.
    ```
    > dir 
    ```
8) 여기에 들어가 보면, 도커 파일이 있다. 그럼 도커 파일을 가지고 도커를 생성할 수 있다.
    ```
    > cd azure-vote 
    ```
9) 컨테이너에 등록하는 작업을 해본다. 그럼 도커의 이미지들이 만들어지는 것을 볼 수 있다.
    ```
    > # az acr build --image azure-vote-front:v1 --registry MyHelmACR --file Dockerfile .  
    > az acr build --image azure-vote-front:v1 --registry labuser2acr --file Dockerfile . # <- 컨테이너에 등록하는 작업까지 한다. 그럼 도커의 이미지들이 만들어지는 것을 볼 수 있다.
    ```

---

### 4. 쿠버네티스에 배포를 하기 위해서 파일을 만든다.

10) Helm을 설치해준다.
    ``` 
    > # https://github.com/helm/helm/releases # <- Helm v3.10.2를 설치해준다.
    > 설치해준 Helm을 C:\Users\kcw0331\azure-voting-app-redis\azure-vote 여기에 카피를 해주었다.(helm을)
    ```
11) 그리고 cmd에서 helm --help를 쳐서 제대로 실행되는지 파악해본다.
    ```
    > helm --help # <- 를 쳐서 help가 실행이 되는지를 확인해본다.
    ```
***

### 5. helm을 이용하기 위해서 YAML을 이용한다.

1)  윈도우 가상환경에서 Notepad에 
```
apiVersion: v2
name: azure-vote-front
description: A Helm chart for Kubernetes

dependencies:
  - name: redis
    version: 14.7.1
    repository: https://charts.bitnami.com/bitnami

...
# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application.
appVersion: v1
```
***

* 아래 있는 거를 저장해준다.

13) 그리고 이거는 쿠버네티스를 함계 뭉쳐서 하는 것이다.
    ```
    > helm create azure-vote-front 
    ```
14) 그리고 이걸 실행해 준다.
    ```
    > helm dependency update azure-vote-front 
    ```
15) azure-vote-front 디렉토리로 이동을 해준다.
    ```
    > cd azure-vote-front
    ```
16) 디렉토리 안에 무엇이 있는지 dir을 사용해서 확인해 준다.
    ```
    > dir
    ```
17) values.yaml안에서 3가지를 수정해 주었다.
    ```
    > notepad values.yaml # <- 여기 안에서 3가지를 수정을 하였다.
    ```
18) 그리고 이걸 실행하게 되면 바로 실행시킬 수 있다. 하지만 path를 제대로 지정을 해주지 않아서 그런지 Azure Portal에는 생성이 되었지만,제대로 실행이 되지 않는 것을 볼 수 있었다.
    ```
    > helm install azure-vote-front azure-vote-front/ # <- 그리고 이걸 실행하게 되면 바로 실행시킬 수 있다. 이걸 실행시킬 때는 azure-vote-front파일로 이동 후 실행을 시켜준다.
    ```

---

https://learn.microsoft.com/ko-kr/azure/aks/quickstart-helm?tabs=azure-cli # <- 마이크로소프트의 이것을 보고 하셨다고 하심.

---

https://learn.microsoft.com/ko-kr/azure/aks/learn/quick-kubernetes-deploy-cli # <- 저녁에 이걸 한번 해보라고 말씀하심.

---

https://learn.microsoft.com/ko-kr/windows/wsl/install # <- wsl을 설치하여 우분투를 설치하는 방법이다.