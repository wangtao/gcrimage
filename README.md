### gcrimage
python code for pull &amp; push images between aliyun and gcr

### requirements
+ **python3**
+ **docker**
+ **aliyun container image server**

### push kubeflow v0.3.5 gcr images to aliyun

you should execute script in google cloud console shell or AWS Server or any server that can access gcr 

`docker login <ALIYUN SERVER>`
`./image_transfer.py -mode push -image images/kubeflow.v0.3.5.list`

### pull from aliyun
`./image_transfer.py -image images/kubeflow.v0.3.5.list`
