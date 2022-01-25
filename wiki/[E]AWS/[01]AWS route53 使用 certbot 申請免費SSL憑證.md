# AWS route53 使用 certbot 申請免費 SSL 憑證

## 安裝 AWS CLI

macOS AWS CLI 的最新版本[下載](https://awscli.amazonaws.com/AWSCLIV2.pkg)，安裝後檢查

```shell
❯ which aws
/usr/local/bin/aws
❯ aws --version
aws-cli/2.4.13 Python/3.8.8 Darwin/21.2.0 exe/x86_64 prompt/off
```

## 設定 AWS CLI

### 首先需要先建立 IAM 使用者專用的存取金鑰

1. 登入 AWS Management Console 的 [IAM 主控台](https://console.aws.amazon.com/iam/)
2. 建立[政策](https://console.aws.amazon.com/iamv2/home#/policies)
   ![建立政策1](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251717859.png)
   ![建立政策2](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251717671.png)
3. 使用剛剛的政策建立群組並建立存取金鑰的使用者
   ![建立使用者1](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251721909.png)
   ![建立群組](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251722835.png)
   ![建立使用者2](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251723326.png)
   ![建立使用者3](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251723535.png)
4. 建立使用者後保存金鑰的值等下會用到
   ![](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251726193.png)

### 設定 AWS CLI

設定

```shell
❯ aws configure
AWS Access Key ID [None]: 存取金鑰ID
AWS Secret Access Key [None]: 私密存取金鑰
Default region name [None]: ap-southeast-1
Default output format [None]: json
```

檢查

```shell
❯ cat ~/.aws/config
[default]
region = ap-southeast-1
output = json
❯ cat ~/.aws/credentials
[default]
aws_access_key_id = 存取金鑰ID
aws_secret_access_key = 私密存取金鑰
```

## 安裝 certbot

```shell
pip install -U certbot certbot_dns_route53
```

## 申請憑證

```shell
❯ certbot certonly --dns-route53 \
 --config-dir "~/cert" \
 --work-dir "~/cert" \
 --logs-dir "~/cert" \
 -d example.com \
 --email nick.yu@example.com \
 --agree-tos
```

## 上傳 aws

```shell
❯ cd cert

❯ aws iam upload-server-certificate --server-certificate-name demo-cert \
    --certificate-body file://live/example.com/cert.pem \
    --private-key file://live/example.com/privkey.pem \
    --certificate-chain file://live/example.com/chain.pem

An error occurred (AccessDenied) when calling the UploadServerCertificate operation: User: arn:aws:iam::xxxxxxxxxxxx:user/certbot-dns-route53-user is not authorized to perform: iam:UploadServerCertificate on resource: arn:aws:iam::xxxxxxxxxxxx:server-certificate/demo-cert
```

## 沒有上傳憑證的權限報錯了，添加權限

```json
{
  "Sid": "VisualEditor2",
  "Effect": "Allow",
  "Action": [
    "iam:GetServerCertificate",
    "iam:UpdateServerCertificate",
    "iam:ListServerCertificates",
    "iam:UploadServerCertificate"
  ],
  "Resource": "*"
}
```

![添加權限](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202201251836094.png)
