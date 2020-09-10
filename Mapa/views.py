from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.files import File
from os import getcwd
from copy import deepcopy
import json


# Create your views here.
@csrf_exempt
def mapa(request):
    # Abro el archivo con el Json
    data = open('Mapa/templates/Mapa/PepitoDonPistola.txt', 'r')
    strData = data.read()
    data.close()
    bigData = json.loads(strData)
    # abro archivo con el html
    html = open('Mapa/templates/Mapa/blockMap.html', 'r')
    strMega = html.read()
    html.close()
    # Abro archivo con los colores
    ids = open('Mapa/templates/Mapa/DonPistolaPepito.txt', 'r')
    strIds = ids.read()
    ids.close()
    idsData = json.loads(strIds)
    
    if (request.method == 'POST'):
        action = request.POST.get('move')
        change = request.POST.get('color')
        if (change != None):
            # Aca modifico el bordeado
            newLine = deepcopy(bigData["colorLine"])
            newLine = newLine.replace(bigData["bordered"], "bor" + change + " ")
            # Aca modifico el html
            strMega = strMega.replace(bigData["colorLine"], newLine)
            strMega = strMega.replace('id="plcol" class= " ' + bigData["btColor"] + ' "', 'id="plcol" class= " col' + change + ' "')
            html = open('Mapa/templates/Mapa/blockMap.html', 'w')
            html.write(strMega)
            html.close()
            # Actualizo el Json
            bigData["colorLine"] = newLine
            bigData["bordered"] = "bor" + change + " "
            bigData["btColor"] = "col" + change
            data = open('Mapa/templates/Mapa/PepitoDonPistola.txt', 'w')
            strData = json.dumps(bigData)
            data.write(strData)
            data.close()
        if (action == "X"):
            newLine = deepcopy(bigData["colorLine"])
            newLine = newLine.replace(bigData["color"], bigData["btColor"])
            strMega = strMega.replace(bigData["colorLine"], newLine)
            # Modifico el Json de colores
            idsData[str(bigData["lineId"])] = bigData["btColor"]
            ids = open('Mapa/templates/Mapa/DonPistolaPepito.txt', 'w')
            strIds = json.dumps(idsData)
            ids.write(strIds)
            ids.close()
            # Modifico el html
            html = open('Mapa/templates/Mapa/blockMap.html', 'w')
            html.write(strMega)
            html.close()
            # Modifico el Json Principal
            bigData["colorLine"] = newLine
            bigData["color"] = deepcopy(bigData["btColor"])
            data = open('Mapa/templates/Mapa/PepitoDonPistola.txt', 'w')
            strData = json.dumps(bigData)
            data.write(strData)
            data.close()
        if (action == "D"):
            # Tomo la linea a la que le voy a sacar el bordeado
            strMega = strMega.replace(bigData["bordered"], "")
            # Agrego el bordeado a la linea derecha
            newLine = bigData["colorLine"]
            if (bigData["lineId"] % 6 == 0):
                blockId =  bigData["lineId"] - 5
            else:
                blockId = bigData["lineId"] + 1
            newLine = newLine.replace("id = ' " + str(bigData["lineId"]) + " '", "id = ' " + str(blockId) + " '")
            newLine = newLine.replace("class = ' " + bigData["color"], "class = ' " + idsData[str(blockId)])
            aux = deepcopy(newLine)
            aux = aux.replace(bigData["bordered"], "")
            strMega = strMega.replace(aux, newLine)
            # Actualizo el Json
            bigData["colorLine"] =  newLine
            bigData["color"] = idsData[str(blockId)]
            bigData["lineId"] = blockId
            data = open('Mapa/templates/Mapa/PepitoDonPistola.txt', 'w')
            strData = json.dumps(bigData)
            data.write(strData)
            data.close()
            # Aca modifico el html
            html = open('Mapa/templates/Mapa/blockMap.html', 'w')
            html.write(strMega)
            html.close()
            return render(request, 'Mapa/blockMap.html')
        if (action == "A"):
            # Tomo la linea a la que le voy a sacar el bordeado
            strMega = strMega.replace(bigData["bordered"], "")
            # Agrego el bordeado a la linea izquierda
            newLine = bigData["colorLine"]
            if (bigData["lineId"] == 1 or bigData["lineId"] == 7 or bigData["lineId"] == 13 or bigData["lineId"] == 19 or bigData["lineId"] == 25 or bigData["lineId"] == 31):
                blockId = bigData["lineId"] + 5
            else:
                blockId = bigData["lineId"] - 1
            newLine = newLine.replace("id = ' " + str(bigData["lineId"]) + " '", "id = ' " + str(blockId) + " '")
            newLine = newLine.replace("class = ' " + bigData["color"], "class = ' " + idsData[str(blockId)])
            aux = deepcopy(newLine)
            aux = aux.replace(bigData["bordered"], "")
            strMega = strMega.replace(aux, newLine)
            # Actualizo el Json
            bigData["colorLine"] =  newLine
            bigData["color"] = idsData[str(blockId)]
            bigData["lineId"] = blockId
            data = open('Mapa/templates/Mapa/PepitoDonPistola.txt', 'w')
            strData = json.dumps(bigData)
            data.write(strData)
            data.close()
            # Aca modifico el html
            html = open('Mapa/templates/Mapa/blockMap.html', 'w')
            html.write(strMega)
            html.close()
            return render(request, 'Mapa/blockMap.html')
        if (action == "S"):
            # Tomo la linea a la que le voy a sacar el bordeado
            strMega = strMega.replace(bigData["bordered"], "")
            # Agrego el bordeado a la linea inferior
            newLine = bigData["colorLine"]
            if (bigData["lineId"] + 6 > 36):
                blockId = bigData["lineId"] - 30
            else:
                blockId = bigData["lineId"] + 6
            newLine = newLine.replace("id = ' " + str(bigData["lineId"]) + " '", "id = ' " + str(blockId) + " '")
            newLine = newLine.replace("class = ' " + bigData["color"], "class = ' " + idsData[str(blockId)])
            aux = deepcopy(newLine)
            aux = aux.replace(bigData["bordered"], "")
            strMega = strMega.replace(aux, newLine)
            # Actualizo el Json
            bigData["colorLine"] =  newLine
            bigData["color"] = idsData[str(blockId)]
            bigData["lineId"] = blockId
            data = open('Mapa/templates/Mapa/PepitoDonPistola.txt', 'w')
            strData = json.dumps(bigData)
            data.write(strData)
            data.close()
            # Aca modifico el html
            html = open('Mapa/templates/Mapa/blockMap.html', 'w')
            html.write(strMega)
            html.close()
            return render(request, 'Mapa/blockMap.html')
        if (action == "W"):
            # Tomo la linea a la que le voy a sacar el bordeado
            strMega = strMega.replace(bigData["bordered"], "")
            # Agrego el bordeado a la linea superior
            newLine = bigData["colorLine"]
            if (bigData["lineId"] - 6 < 1):
                blockId = bigData["lineId"] + 30
            else:
                blockId = bigData["lineId"] - 6
            newLine = newLine.replace("id = ' " + str(bigData["lineId"]) + " '", "id = ' " + str(blockId) + " '")
            newLine = newLine.replace("class = ' " + bigData["color"], "class = ' " + idsData[str(blockId)])
            aux = deepcopy(newLine)
            aux = aux.replace(bigData["bordered"], "")
            strMega = strMega.replace(aux, newLine)
            # Actualizo el Json
            bigData["colorLine"] =  newLine
            bigData["color"] = idsData[str(blockId)]
            bigData["lineId"] = blockId
            data = open('Mapa/templates/Mapa/PepitoDonPistola.txt', 'w')
            strData = json.dumps(bigData)
            data.write(strData)
            data.close()
            # Aca modifico el html
            html = open('Mapa/templates/Mapa/blockMap.html', 'w')
            html.write(strMega)
            html.close()
            return render(request, 'Mapa/blockMap.html')
        return render(request, 'Mapa/blockMap.html')
    return render(request, 'Mapa/blockMap.html')
