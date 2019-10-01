import serial
with serial.Serial('COM12', 57600, timeout=3) as ser:

    while(True):
        line = ser.readline()
        if(b'+CMTI: "SM",' in line):
            index = line[12:]
            index = str(index,"utf-8")
            new_index = ""
            for i in index:
                if(i != "\\r\\n"):
                    new_index = new_index+i
            new_index = int(new_index)
            new = "AT+CMGR={}\r\n".format(new_index)
            new = bytes(new,"utf-8")
            ser.write(new)
            query = ser.read(200)
            print(query)
            
    
 
