from bottle import *
import os

@route('/')
def index():
    return '''
    <h2>Verkefni 3</h2>
    <a href="1">Liður 1</a>
    <a href="2">Liður 2</a>
    '''

folk = [["Haldór Atli",2304994399],
        ["Jón Páll",1104004530],
        ["Jón Ásgeir",2306913459],
        ["Jón Gnarr",3003998789]]
@route('/1')
def lidur1():
    return template('v2/lidur1', folk=folk)

@route('/kt/<kennitala>')
def lidur1(kennitala):
    return template('v2/kennitala', kt=kennitala)

adalFrettir = [["Níu fugla dagur", 1],
               ["Klassískur G-Class fær uppfærslu", 2],
               ["3 í haldi vegna send­ing­ar á Skák­sam­bandið", 3],
               ["Flughált sums staðar á landinu", 4]]
@route('/2')
def lidur2():
    return template('v2/lidur2', frettir=adalFrettir)

frettirnar = [{"titill":"Níu fugla dagur","grein":"Ólafía Þórunn Kristinsdóttir endaði i 26. sæti á Pure Silk mótinu á Bahamaeyjum sem lauk í gær.","netfang":"ritari1@Bestufrettirnar.is","mynd":"golf.png"},
              {"titill":"Klassískur G-Class fær uppfærslu","grein":"Er 170 kílóum léttari en samt lengri og breiðari. Nýr G-Class heldur áfram sínu klassíska útliti sem hann hefur haft síðan hann var fyrst kynntur til sögunnar árið 1979.","netfang":"ritari2@Bestufrettirnar.is","mynd":"benz.png"},
              {"titill":"3 í haldi vegna send­ing­ar á Skák­sam­bandið","grein":"Þrír ein­stak­ling­ar eru nú í gæslu­v­arðhaldi vegna rann­sókn­ar á inn­flutn­ingi fíkni­efna í send­ingu sem merkt var Skák­sam­bandi Íslands. „Rann­sókn­in er í þokka­leg­um far­vegi,“ seg­ir Mar­geir Sveins­son hjá rann­sókn­ar­deild lög­regl­unn­ar á höfuðborg­ar­svæðinu. „Við erum að vinna í þessu.“","netfang":"ritari1@Bestufrettirnar.is","mynd":"logreglan.png"},
              {"titill":"Flughált sums staðar á landinu","grein":"Hálka er á vegum víða um land í dag og sums staðar snjóþekja. Vegagerðin varar við því að flughált geti verið á útvegum á Suður- og Suðvesturlandi, í Borgarfirði og víða á Norður- og Austurlandi. Spáð er frostlausu veðri við suður- og vesturströndina í dag en frosti annars staðar.","netfang":"ritari3@Bestufrettirnar.is","mynd":"halt.png"}]
@route('/frett/<numer>')
def frett(numer):
    return template('v2/frett', frettirnar[int(numer)-1])

@route('/css/<skjal>')
def server_static(skjal):
    return static_file(skjal, root='./v2/css')

@route('/myndir/<skjal>')
def server_static(skjal):
    return static_file(skjal, root='./v2/myndir')

@error(404)
def villa(error):
    return '''
    <h2>Error 404</h2>
    <h3>Síða finnst ekki</h3>
    <a href="/">Til Baka</a>
    '''
@error(500)
def villa(error):
    return '''
    <h2>Error 500</h2>
    <h3>Vill í forritinu</h3>
    <a href="/">Til Baka</a>
    '''

run(host="0.0.0.0", port=os.environ.get('PORT'))
