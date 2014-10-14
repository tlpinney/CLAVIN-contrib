# CLAVIN Python API

## Prerequisites 

pip install -r requirements.txt

## Usage

    from clavin import Clavin
    
    # connect to CLAVIN REST service  
    clv = Clavin("http://localhost:9090/api/v0/geotag")

    # resolve locations in document and output results to stdout
    doc = open("document.txt","r").read()    
    res = clv.resolve(doc)
    print res 








