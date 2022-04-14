# 몽고 DB

## 1. 질의

- 하나의 쿼리를 명시하는 키워드

- mongoDB는 6개 정도의 질의를 가진다.



### 1.1 키 - 값 질의

특정필드와 맵핑되는 값을 포함하는 문서 `{}`를 말한다.

주 Key에 대한 값을 리턴하는 경우



### 1.2 범위

특정 범위에 포함되는 값을 말함. (비교연산자)



### 1.3 공간질의

선, 원, 다각형 등에 대한 공간 근사값



### 1.4 문자열 탐색질의

논리연산자를 통해서 특정 문자열을 탐색



### 1.5 집합 질의

그룹함수를 지칭하며 count, min, max, average 등을 이용한 결과값



### 1.6 MR (MapReduce Query)

파일, DB 등의 데이터를 가져다가 데이터(value)를 뽑아서 분철(1값 부여) 후 정렬, 집계한다. (combine 작업)

이 작업의 속도가 얼마나 빠른지에 따라 성능을 말한다.

분산 시스템들은 MR을 얼마나 효율적으로 하는지가 제일 중요.

javascript로 표현되는 복잡한 데이터를 데이터 베이스로 실행 해 반환하는 질의



## 2. 컬렉션 규칙 및 키에 대한 필드명 생성 조건

컬렉션은 RDB의 테이블과 같다.

- 2.1 `$`로 시작할 수 없다.

- 2.2 255이내로 작성한다.

- 2.3 `.` 연산자를 포함 할 수 없다.

- 2.4 공백이 중간에 들어갈 수 없다.

- 2.5 필드 이름은 하나의 컬렉션 내에서 유일한 값으로 존재한다.

- 2.6 전체 문서의 크기가 16M로 제한적이다. (네트워크 대역폭이 16M로 제한되어 있음)

- 2.7 만일 문서가 대용량(16M 이상)이면 GridFS api(대용량 데이터 처리)를 사용해서 구현한다.



데이터를 다룬다면 txt, sql, csv, tsv, xml, json은 서로서로 호환되게 구현(변환)할 수 있어야한다.



## 3. 문서에 대한 정보 (외부적인 상태)

- 3.1 mongod.lock : 서버의 프로세스 ID 저장한다.
- 3.2 `.0 파일 (.ns)` : 메타 데이터를 네임스페이스 단위로 저장한다.
- 3.3 2번의 크기는 ns 16M를 넘을 수 없다.  (28000개 정도의 네임스페이스) 
  (하나의 데이터베이스는 컬렉션과 색인수를 최대 28000개를 가진다.)
  `--nssize arg(=16)` 
- 3.4 `test.0`(64M), `test.1`(128M) 식으로 데이터 저장소를 확보해서 데이터를 저장한다라고 간주 한다면 파일의 용량은 2GB까지가 최대이다.
- 3.5 몽고는 데이터 저장소 크기를 정적으로 관리한다.



ex) 확인

`C:\Program Files\MongoDB\Server\4.4\bin\mongod.exe" --config "C:\Program Files\MongoDB\Server\4.4\bin\mongod.cfg" --service`

mongod.cfg를 열어보면

```
# mongod.conf

# for documentation of all options, see:
#   http://docs.mongodb.org/manual/reference/configuration-options/

# Where and how to store data.
storage:
  dbPath: C:\Program Files\MongoDB\Server\4.4\data # 실제 저장소
  journal:
    enabled: true
#  engine:
#  mmapv1:
#  wiredTiger:

# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path:  C:\Program Files\MongoDB\Server\4.4\log\mongod.log # 로그 패스

# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1


#processManagement:

#security:

#operationProfiling:

#replication:

#sharding:

## Enterprise-Only Options:

#auditLog:

#snmp:

```





## 4. 문서에 대한 정보 (내부적인 상태)

`--db.stats(1042);` : 자료를 입력했을 때 몽고 드라이버가 동작된 후 데이터 상태확인

자료를 입력 했을 때 몽고 드라이버가 동작된다.

- 4.1 mongodb에 삽입되는 문서의 고유 번호 ID인 `_id`로 필드와 값을 생성한다.

- 4.2 문서를 mongodb의 bson으로 변환한다.
- 4.3 네트워크 소켓을 이용해서 데이터베이스를 전달한다.



---





<실습>

1. 서비스에서 mongo 서버를 중단

2. C:\data\mydata 생성 후 my.log, my.cfg 파일을 생성한다.
   C:\data\log\my.log
   C:\data\cfg\my.cfg

3. 해당 로그 파일을 저장 할 때 사용자가 지정하는 특정 위치를 사용하도록 지정한다.
   cmd 관리자에서 다음 명령을 친다.

   ```
   echo logpath = "C:\data\log\my.log" > "C:\data\cfg\my.cfg"
   ```

4. db path를 지정한다. 서비스에 이름도 등록하자.

   C:\ > mongod --dbpath "C:\data\mydata" --logpath "C:\data\cfg\my.cfg" --install --serviceName MyMongo --serviceDisplayName MyMongo

5. 삭제
   c:\ > mongod --dbpath "C:\data\mydata" --logpath "C:\data\cfg\my.cfg" --remove

6. c:\ > Net start MyMongo (시작)

   c:\ > Net stop MyMongo (중지)

>참고로 cmd를 관지자권한으로 해야 서비스에 올라온다...





```
C:\Users\Jay>mongo
MongoDB shell version v4.4.13
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("9392d3af-e0b2-4a43-8d07-c545a81ea94a") }
MongoDB server version: 4.4.13
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        https://docs.mongodb.com/
Questions? Try the MongoDB Developer Community Forums
        https://community.mongodb.com
---
The server generated these startup warnings when booting:
        2022-04-13T12:41:43.986+09:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
        2022-04-13T12:41:43.986+09:00: This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind_ip <address> to specify which IP addresses it should serve responses from, or with --bind_ip_all to bind to all interfaces. If this behavior is desired, start the server with --bind_ip 127.0.0.1 to disable this warning
---
---
        Enable MongoDB's free cloud-based monitoring service, which will then receive and display
        metrics about your deployment (disk utilization, CPU, operation statistics, etc).

        The monitoring data will be available on a MongoDB website with a unique URL accessible to you
        and anyone you share the URL with. MongoDB may use this information to make product
        improvements and to suggest MongoDB products and deployment options to you.

        To enable free monitoring, run the following command: db.enableFreeMonitoring()
        To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
```

mongo로 접속하면 접속 아이피와 포트가 뜸.

`connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb`



접속하면 세션이 생긴다.

`Implicit session: session { "id" : UUID("9392d3af-e0b2-4a43-8d07-c545a81ea94a") }`

cmd창을 여러개 띄우고 mongo실행시 각 세션이 생기는데 다 UUID(클라이언트 아이디)가 다 다르다. 몽고 입장에선 각각의 클라이언트들이 접속했다고 보는 것.





```
> help
        db.help()                    help on db methods
        db.mycoll.help()             help on collection methods
        sh.help()                    sharding helpers
        rs.help()                    replica set helpers
        help admin                   administrative help
        help connect                 connecting to a db help
        help keys                    key shortcuts
        help misc                    misc things to know
        help mr                      mapreduce

        show dbs                     show database names
        show collections             show collections in current database
        show users                   show users in current database
        show profile                 show most recent system.profile entries with time >= 1ms
        show logs                    show the accessible logger names
        show log [name]              prints out the last segment of log in memory, 'global' is default
        use <db_name>                set current database
        db.mycoll.find()             list objects in collection mycoll
        db.mycoll.find( { a : 1 } )  list objects in mycoll where a == 1
        it                           result of the last line evaluated; use to further iterate
        DBQuery.shellBatchSize = x   set default number of items to display on shell
        exit                         quit the mongo shell
```



뭐 일단 건들인거 하나도 없음 (만든게 없음)

```
> db.help() # db에 대한 도움말

DB methods:
        db.adminCommand(nameOrDocument) - switches to 'admin' db, and runs command [just calls db.runCommand(...)]
        db.aggregate([pipeline], {options}) - performs a collectionless aggregation on this database; returns a cursor
        db.auth(username, password)
        db.cloneDatabase(fromhost) - will only function with MongoDB 4.0 and below
        db.commandHelp(name) returns the help for the command
        db.copyDatabase(fromdb, todb, fromhost) - will only function with MongoDB 4.0 and below
        db.createCollection(name, {size: ..., capped: ..., max: ...})
        db.createUser(userDocument)
        db.createView(name, viewOn, [{$operator: {...}}, ...], {viewOptions})
        db.currentOp() displays currently executing operations in the db
        db.dropDatabase(writeConcern)
        db.dropUser(username)
        db.eval() - deprecated
        db.fsyncLock() flush data to disk and lock server for backups
        db.fsyncUnlock() unlocks server following a db.fsyncLock()
        db.getCollection(cname) same as db['cname'] or db.cname
        db.getCollectionInfos([filter]) - returns a list that contains the names and options of the db's collections
        db.getCollectionNames()
        db.getLastError() - just returns the err msg string
        db.getLastErrorObj() - return full status object
        db.getLogComponents()
        db.getMongo() get the server connection object
        db.getMongo().setSecondaryOk() allow queries on a replication secondary server
        db.getName()
        db.getProfilingLevel() - deprecated
        db.getProfilingStatus() - returns if profiling is on and slow threshold
        db.getReplicationInfo()
        db.getSiblingDB(name) get the db at the same server as this one
        db.getWriteConcern() - returns the write concern used for any operations on this db, inherited from server object if set
        db.hostInfo() get details about the server's host
        db.isMaster() check replica primary status
        db.hello() check replica primary status
        db.killOp(opid) kills the current operation in the db
        db.listCommands() lists all the db commands
        db.loadServerScripts() loads all the scripts in db.system.js
        db.logout()
        db.printCollectionStats()
        db.printReplicationInfo()
        db.printShardingStatus()
        db.printSecondaryReplicationInfo()
        db.resetError()
        db.runCommand(cmdObj) run a database command.  if cmdObj is a string, turns it into {cmdObj: 1}
        db.serverStatus()
        db.setLogLevel(level,<component>)
        db.setProfilingLevel(level,slowms) 0=off 1=slow 2=all
        db.setVerboseShell(flag) display extra information in shell output
        db.setWriteConcern(<write concern doc>) - sets the write concern for writes to the db
        db.shutdownServer()
        db.stats()
        db.unsetWriteConcern(<write concern doc>) - unsets the write concern for writes to the db
        db.version() current version of the server
        db.watch() - opens a change stream cursor for a database to report on all  changes to its non-system collections.
```

```
> db.stats()
{
        "db" : "test", #이름을 안줘도 test로 자동 생성
        "collections" : 0,
        "views" : 0,
        "objects" : 0,
        "avgObjSize" : 0,
        "dataSize" : 0,
        "storageSize" : 0,
        "totalSize" : 0,
        "indexes" : 0,
        "indexSize" : 0,
        "scaleFactor" : 1,
        "fileSize" : 0,
        "fsUsedSize" : 0,
        "fsTotalSize" : 0,
        "ok" : 1
}
```



```
> db.hostInfo()
{
        "system" : {
                "currentTime" : ISODate("2022-04-13T03:57:23.802Z"),
                "hostname" : "DESKTOP-4ACWLQO",
                "cpuAddrSize" : 64,
                "memSizeMB" : NumberLong(32445),
                "memLimitMB" : NumberLong(32445),
                "numCores" : 8,
                "cpuArch" : "x86_64",
                "numaEnabled" : false
        },
        "os" : {
                "type" : "Windows",
                "name" : "Microsoft Windows 10",
                "version" : "10.0 (build 19042)"
        },
        "extra" : {
                "pageSize" : NumberLong(4096),
                "physicalCores" : 4
        },
        "ok" : 1 # ok=1이 반환되면 성공, 아니면 뭔가에서 fail뜬거
}
```





---

테이블을 생성 한 후 데이터를 입력 해보자.

```sql
CREATE TABLE MY(
	USER_ID VARCHAR2(20), AGE NUMBER, STATUS VARCHAR2(5));
INSERT INTO MY VALUES('AAA', 23, 'A')
```



```
db.exam.insert({a:"a"})
db.exam.find()
```

