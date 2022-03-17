# --------------------------------------------------------------------------- # 
# configure the client logging
# --------------------------------------------------------------------------- # 
import json
import logging
import os
import random
from datetime import date, datetime
from sys import path
from time import sleep
import asyncio

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

import defs
import vars

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

ORDER_DICT = {
    "<": "LITTLE",
    ">": "BIG"
}

def insert_values_modbus(ip, port):
    print("Method insert_values_modbus start...")
    print("Method insert_values_modbus connect server...")    

    while(True):
        try:
            client = ModbusClient(ip=vars.ip, port=vars.port)
            client.host = defs.get_ip_modbus()
            client.port = defs.get_port_modbus()
            if client.connect():
                va = vars.initial_address_modbus        
                while (va <= vars.final_address_modbus):
                    print("Method insert_values_modbus server connected " + str(client.connect()))
                    client.write_registers(va, random.randint(0,65535))
                    va += 1                
                print("Method insert_values_modbus finish...")
                print("-" * 60)            
                client.close()
                print("Method insert_values_modbus finish...")     
            else:
                print("Method insert_values_modbus server not connected.")
        except:
            continue
        finally:        
            sleep(60)

def get_values_modbus_client(ip, port, fileName, address):
    try:
        print("Method get_values_modbus_client start...")
        print("Method get_values_modbus_client connect server...")
        
        while (True):        
            client = ModbusClient(ip=vars.ip, port=vars.port)
            client.host = defs.get_ip_modbus()
            client.port = defs.get_port_modbus()
            if client.connect():
                print("Method get_values_modbus_client server connected " + str(client.connect()))
                # insert_result = client.write_registers(random.randint(5001,5181), random.randint(0,65535))

                if os.path.isfile(fileName + vars.extension_json):
                    with open(str(fileName) + vars.extension_json, 'r') as arq:
                        obj = json.load(arq)
                else:
                    print('\nO arquivo {} não foi encontrado. Por favor, receba o arquivo via método direto: Receives tags. \n'.format(fileName + vars.extension_json))
                    return

                if os.path.isfile(vars.fn_values_tags + vars.extension_json):
                    with open(vars.fn_values_tags + vars.extension_json, 'r') as arqtelemetry:
                        objtelemetry = json.load(arqtelemetry)                    
                        filetelemetry = arqtelemetry
                        str_json = objtelemetry
                else:
                    str_json = {}

                # if os.path.isfile(vars.path_values_tags + '/' + vars.fn_values_tags + vars.extension_json):
                #     with open(vars.path_values_tags + '/' + vars.fn_values_tags + vars.extension_json, 'r') as arqtelemetry:
                #         objtelemetry = json.load(arqtelemetry)                    
                #         filetelemetry = arqtelemetry
                #         str_json = objtelemetry
                # else:
                #     str_json = {}
                #     filetelemetry = None

                
                
                date = datetime.now().timestamp()
                if str_json == {}:                
                    for tags in obj[str(fileName)].items():
                        tagName = tags[0]
                        tagProperty = tags[1]
                        tagModbusAddress = tagProperty[vars.field_ds_endereco_modbus]                
                        result = client.read_holding_registers(tagModbusAddress-1, 1, unit=1) 
                        str_json[tagName] = [{"value": result.registers[0], vars.field_dt_modbus: date}]
                else:
                    
                    for tags in obj[str(fileName)].items():
                        tagName = tags[0]
                        tagProperty = tags[1]
                        tagModbusAddress = tagProperty[vars.field_ds_endereco_modbus]                
                        result = client.read_holding_registers(tagModbusAddress-1, 1, unit=1) 
                        s = {tagName: {"value": result.registers[0], vars.field_dt_modbus: date}}
                        defs.updateToJSONFile('./',vars.fn_values_tags,s)
                        # objtelemetry.update({tagName [{"value": result.registers[0], vars.field_dt_modbus: date}]})

                    filetelemetry.seek(0)
                    json.dump(objtelemetry, filetelemetry)
                            
                defs.writeToJSONFile('./',vars.fn_values_tags,str_json)
                result = client.read_holding_registers(address, 127, unit=1)
                result2 = client.read_holding_registers(5127, 54, unit=1)
                print("-" * 60)
                print("Registers - Start")
                print("-" * 60)
                print(result.registers)
                print(result2.registers)
                print("-" * 60)
                print("Registers - Finish")
                print("-" * 60)                        
                client.close()
                print("Method get_values_modbus_client finish...")
            else:
                print("Method get_values_modbus_client server not connected.")
            
            sleep(60) # time in seconds
    except:
        print('Except: get_values_modbus_client') 

async def get_value_modbus(client):
    while (True):
        try:
            print("Method get_value_modbus start...")
            print("Method get_value_modbus connect server...")
            if(defs.is_disable_module() == True):
                continue

            fn_asset = defs.get_file_name_asset()
            if (fn_asset == None):
                print('\nNão foi encontrado nenhum arquivo de configuração com ativos')                
                continue
            if (len(fn_asset) <= 0):
                print('\nNão foi encontrado nenhum arquivo de configuração com ativos')
                continue

            for name in fn_asset:
                vars.fn_asset = name.replace('.json', '')

                modbus_client = ModbusClient(ip=vars.ip, port=vars.port)
                modbus_client.host = defs.get_ip_modbus()
                modbus_client.port = defs.get_port_modbus()
                if modbus_client.connect():
                    print("Method get_value_modbus server connected " + str(modbus_client.connect()))
                    
                    obj = defs.readJSONFile(vars.path_asset, vars.fn_asset)
                    if(obj == None):
                        print('\nO arquivo {} não foi encontrado. Por favor, receba o arquivo via método direto: Receives tags. \n'.format(vars.fn_asset + vars.extension_json))
                        break
                    
                    js_sendind_last = defs.readJSONFile(vars.path_sending_last, vars.fn_sending_last)
                    if(js_sendind_last == None):
                        js_sendind_last = {}
                        new_send_last = True
                    else:
                        new_send_last = False

                    if(defs.set_min_max_address_modbus(vars.fn_asset) == False):
                        print('\nProblemas ao buscar o endereçamento menor e maior modbus para o arquivo {}. \n'.format(vars.fn_asset + vars.extension_json))
                        break

                    filetelemetry = objtelemetry = defs.readJSONFile(vars.path_values_tags, vars.fn_values_tags)
                    if(objtelemetry == None):
                        str_json = {}
                    else:
                        str_json = objtelemetry
                        if(len(objtelemetry) <= 4):
                            os.remove(os.getcwd() + '/' + vars.path_values_tags + '/' + vars.fn_values_tags + vars.extension_json)
                            filetelemetry = None
                            objtelemetry = None
                                
                    date = datetime.now().timestamp()
                    alarm = alarmTelemetry = False                    
                    str_json = {vars.field_tp_estacao: obj[vars.field_tp_estacao], vars.field_tp_regiao: obj[vars.field_tp_regiao], vars.field_tp_subregiao: obj[vars.field_tp_subregiao], "alarm": "{}".format(alarm)}
                    n1 = obj[vars.field_tp_regiao]
                    n2 = obj[vars.field_tp_subregiao]
                    for tags in obj[n1][n2][vars.fn_asset].items():                
                        tagName = tags[0]
                        tagProperty = tags[1]
                        tagModbusAddress = tagProperty[vars.field_ds_endereco_modbus]
                        tagDataType = tagProperty[vars.field_tp_dado_tag]
                        tagFrequency = tagProperty[vars.field_vl_frequencia_envio_tag]
                        tagModbusAddressWriting = tagProperty[vars.field_ds_endereco_modbus_escrita]
                        tagStatusModbusWriting = tagProperty[vars.field_fl_envio_status_modbus_escrita]
                        
                        modbusValue = get_value_modbus_server(modbus_client, tagModbusAddress, tagDataType)
                        limitLow = defs.get_limit(tagName, vars.field_vl_limite_minimo)
                        limitHigh = defs.get_limit(tagName, vars.field_vl_limite_maximo)
                        if(tagDataType == "Boolean"):
                            alarmTelemetry = False
                        else:
                            if(limitLow != None and limitHigh != None):
                                if(modbusValue < limitLow or modbusValue > limitHigh):                        
                                    alarm = alarmTelemetry = True
                                else:
                                    alarmTelemetry = False
                            else:
                                alarmTelemetry = False

                        # if(alarmTelemetry == True):
                        js_alarmTelemetry = {
                                                vars.field_tp_estacao: obj[vars.field_tp_estacao], 
                                                vars.field_tp_regiao: obj[vars.field_tp_regiao], 
                                                vars.field_tp_subregiao: obj[vars.field_tp_subregiao], 
                                                "alarm": "{}".format(alarmTelemetry),
                                                tagName: {
                                                            "telemetry": [
                                                                {
                                                                    "value": modbusValue, 
                                                                    vars.field_dt_modbus: date, 
                                                                    "alarm": "{}".format(alarmTelemetry)
                                                                }
                                                            ]
                                                        }
                                            }
                        await defs.send_telemetry_alarm(client, js_alarmTelemetry, tagName, alarmTelemetry, tagModbusAddressWriting, tagStatusModbusWriting)

                        if (defs.is_modbus_value_search(tagName, tagFrequency, date) == False):
                            continue

                        # if (defs.is_modbus_value_search(tagName, tagFrequency, date) == False):
                        #     if(alarmTelemetry == False):
                        #         continue
                        #     if(alarmTelemetry == True and (defs.get_sending_last_alarm(tagName, date) == True)):
                        #         continue

                        if filetelemetry == None:
                            str_json[tagName] = {"telemetry": [{"value": modbusValue, vars.field_dt_modbus: date, "alarm": "{}".format(alarmTelemetry)}]}
                        else:
                            s = {tagName: {"value": modbusValue, vars.field_dt_modbus: date, "alarm": "{}".format(alarmTelemetry)}}
                            s2 = {tagName: {"telemetry": [{"value": modbusValue, vars.field_dt_modbus: date, "alarm": "{}".format(alarmTelemetry)}]}}
                            defs.updateToJSONFile(vars.path_values_tags, vars.fn_values_tags, s, True, s2)
                            
                        js_sendind_last[tagName] = {vars.field_dt_modbus: date, "alarm": "{}".format(alarmTelemetry)}

                    if(filetelemetry == None):                
                        defs.writeToJSONFile(vars.path_values_tags, vars.fn_values_tags, str_json)
                    # else:
                    #     values_tags_file = defs.readJSONFile(vars.path_values_tags, vars.fn_values_tags)
                    #     if(values_tags_file != None):
                    #         if(str(values_tags_file["alarm"]) != str(alarm) and (len(values_tags_file) > 4)):
                    #             values_tags_file["alarm"] = "{}".format(alarm)
                    #             defs.updateToJSONFile(vars.path_values_tags, vars.fn_values_tags, values_tags_file, False, {}, True)
                    
                    if(new_send_last == True):
                        defs.writeToJSONFile(vars.path_sending_last, vars.fn_sending_last, js_sendind_last)
                    else:
                        defs.updateToJSONFile(vars.path_sending_last, vars.fn_sending_last, js_sendind_last)

                    # if(alarm):
                    #     if(filetelemetry != None):                    
                    #         defs.updateToJSONFile(vars.path_values_tags, vars.fn_values_tags, str_json)
                        
                    #     await defs.send_telemetry(client) # Envia o novo pacote
                    
                    modbus_client.close()
                    print("Method get_value_modbus finish...")
                else:
                    print("Method get_value_modbus server not connected.")                    
        except Exception as e:
            print("Except: get_value_modbus.\nError: ")
            print(e)
            continue
        finally:
            await asyncio.sleep(vars.sleep_modbus_search_frequency) # time in seconds

async def modbus_server_is_connected(client):
    while (True):
        try:
            print("Method modbus_server_is_connected start...")
            print("Method modbus_server_is_connected connect server...")
            if(defs.is_disable_module() == True):
                continue

            connection_modbus_time = datetime.now().timestamp()
            modbuslastsend_file = defs.readJSONFile(vars.path_modbus, vars.fn_modbus_last_send)
            modbus_client = ModbusClient(ip=vars.ip, port=vars.port)
            modbus_client.host = defs.get_ip_modbus()
            modbus_client.port = defs.get_port_modbus()
            modbus_connected = modbus_client.connect()

            if(modbuslastsend_file != None):
                modbuslastsend_status_file = modbuslastsend_file["modbus_server_is_connected"]
                if (modbuslastsend_status_file == modbus_connected):
                    continue

            js = {"modbus_server_is_connected": modbus_connected, vars.field_dt_conexao_modbus: connection_modbus_time}
            defs.writeToJSONFile(vars.path_modbus, "{}_{}".format(vars.fn_modbus, connection_modbus_time), js)
            defs.writeToJSONFile(vars.path_modbus, vars.fn_modbus_last_send, {"modbus_server_is_connected": modbus_connected})
            
            # if modbus_connected:
            #     print("Method modbus_server_is_connected server connected " + str(modbus_connected))                                                            
            #     modbus_client.close()
            #     await defs.send_connection_modbus(client, True, datetime.now().timestamp())                
            # else:
            #     print("Method modbus_server_is_connected server is not connected")
            #     await defs.send_connection_modbus(client, False, datetime.now().timestamp())
        except:
            continue
        finally:
            print("Method modbus_server_is_connected finish...")
            await asyncio.sleep(vars.sleep_modbus_search_frequency) # time in seconds

def get_value_modbus_server(client, tagModbusAddress, tagDataType):
    try:
        count = 1
        if tagDataType == "Boolean":
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_bits()    
        elif tagDataType == "Float16":        
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_16bit_float()
        elif tagDataType == "Float32":        
            count = 2
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_32bit_float()
        elif tagDataType == "Float64":
            count = 4
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_64bit_float()
        elif tagDataType == "Int16":        
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_16bit_int()
        elif tagDataType == "Int32":
            count = 2
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_32bit_int()
        elif tagDataType == "Int64":
            count = 4
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_64bit_int()
        elif tagDataType == "Uint16":        
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_16bit_uint()
        elif tagDataType == "Uint32":
            count = 2
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_32bit_uint()
        elif tagDataType == "Uint64":
            count = 4
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_64bit_uint()
        elif tagDataType == "String":
            count = 1 # Rafa, nesse caso como saberei quantas casas?
            result = client.read_holding_registers(tagModbusAddress, count, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
            return decoder.decode_string()        
    except:
        print('Except: get_value_modbus_server')
        
def insert_alarm_value_modbus(modbusAddress, modbusValue):
    try:
        print("Method insert_alarm_value_modbus start...")
        client = ModbusClient(ip=vars.ip, port=vars.port)
        client.host = defs.get_ip_modbus()
        client.port = defs.get_port_modbus()
        if client.connect():
            client.write_registers(modbusAddress, modbusValue)
            client.close()
        else:
            print("Method insert_alarm_value_modbus server not connected.")
    except Exception as e:
        print("Except: insert_alarm_value_modbus.\nError: {}".format(e))
        pass
    finally:
        print("Method insert_alarm_value_modbus finish...")

# if __name__ == "__main__":
#     # insert_values_modbus(vars.ip, vars.port)
