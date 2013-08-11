Experimental CLAVIN Scala web server
=====================================


## Prerequisites 

Play framework 

http://www.playframework.com/

CLAVIN 0.3.4 - https://github.com/Berico-Technologies/CLAVIN/tree/release/0.3.4

    git clone https://github.com/Berico-Technologies/CLAVIN.git
    cd CLAVIN
    git checkout 0.3.4 
    curl http://download.geonames.org/export/dump/allCountries.zip -o allCountries.zip
    unzip allCountries.zip 
    mvn compile
    # build the index  
    MAVEN_OPTS="-Xmx2048M" mvn exec:java -Dexec.mainClass="com.berico.clavin.index.IndexDirectoryBuilder"
    mvn package 
        


## Point to the correct index directory
  
    git clone https://github.com/Berico-Technologies/CLAVIN-contrib
    cd CLAVIN-contrib/clavin-server 

Edit conf/application.conf and put in the correct index path 

    clavin.index = "/Users/tpinney/project/CLAVIN/IndexDirectory"

## Start the server 

    play run 


## Send a document to the REST service

Sample document of the wikipedia Yak article 

    curl -H"Content-Type:text/plain" -d@document.txt http://localhost:9000

This will return JSON of the resolved locations 


## Experimental Python REST API 
 
    CLAVIN-contrib/clavin-server 


## Known issues 

First REST call returns an error, everything after that is fine.

    [error] play - Oops, unexpected message received in NettyServer (please report this problem): org.jboss.netty.handler.codec.http.DefaultHttpChunk@9d14a9
    [error] play - Oops, unexpected message received in NettyServer (please report this problem): org.jboss.netty.handler.codec.http.DefaultHttpChunk@1b24e0f2
    [error] play - Oops, unexpected message received in NettyServer (please report this problem): org.jboss.netty.handler.codec.http.DefaultHttpChunk@168ca218
    [error] play - Oops, unexpected message received in NettyServer (please report this problem): org.jboss.netty.handler.codec.http.DefaultHttpChunk@a4f5b6d
    [error] play - Oops, unexpected message received in NettyServer (please report this problem): org.jboss.netty.handler.codec.http.DefaultHttpChunk@6de4f076
    [error] play - Oops, unexpected message received in NettyServer (please report this problem): org.jboss.netty.handler.codec.http.DefaultHttpChunk@79b933a5
    [error] play - Oops, unexpected message received in NettyServer (please report this problem): org.jboss.netty.handler.codec.http.HttpChunk$1@6519ceb1


