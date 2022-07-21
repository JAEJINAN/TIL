# elk 설치

## ubuntu 18.04 LTS



## 설치 명령어

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

sudo apt-get install apt-transport-https

echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list

sudo apt-get update && sudo apt-get install elasticsearch
```



## 설정

```bash
sudo vi /etc/elasticsearch/elasticsearch.yml
```

vi로 들어가서 `node.name`, `network.host` 주석을 해제해주고, network.host의 아이피를 `0.0.0.0`으로 바꿔주자.

`discovery.seed_hosts`를 ["127.0.0.1"]로 바꿔주고,
`cluster.initial_master_nodes`에서 ["node-1"]로 해주자.



```bash
# ...
node.name: node-1
# ...
network.host: 0.0.0.0
# ...
discovery.seed_hosts: ["127.0.0.1"]
# ...
cluster.initial_master_nodes: ["node-1"]
```

그 후 `esc + :wq` 저장 후 나오자.



## 시작

```bash
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable elasticsearch.service

sudo /bin/systemctl start elasticsearch.service

curl -XGET 127.0.0.1:9200
```

데이터 다운 및 넣기

```bash
wget http://media.sundog-soft.com/es7/shakes-mapping.json

curl -H "Content-Type: application/json" -XPUT 127.0.0.1:9200/shakespeare --data-binary @shakes-mapping.json

wget http://media.sundog-soft.com/es7/shakespeare_7.0.json

curl -H "Content-Type: application/json" -XPOST '127.0.0.1:9200/shakespeare/_bulk' --data-binary @shakespeare_7.0.json
```

