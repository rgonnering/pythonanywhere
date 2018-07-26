
# -*- coding: utf-8 -*-
# data.py

present_tense = [
[u'hablar' , u'to speak; talk' , u'hablo' , u'hablas' , u'habla' , u'hablamos' , u'habláis' , u'hablan' ],
[u'comer' , u'to eat; feed' , u'como' , u'comes' , u'come' , u'comemos' , u'coméis' , u'comen' ],
[u'escrebir' , u'to write' , u'escrebo' , u'escrebes' , u'escrebe' , u'escrebimos' , u'escrebís' , u'escreben' ],
[u'pagar' , u'to pay' , u'pago' , u'pagas' , u'paga' , u'pagamos' , u'pagáis' , u'pagan' ],
[u'tocar' , u'to touch; play an instrument' , u'toco' , u'tocas' , u'toca' , u'tocamos' , u'tocáis' , u'tocan' ],
[u'almorzar' , u'to (have) lunch' , u'almuerzo' , u'almuerzas' , u'almuerza' , u'almorzamos' , u'almorzáis' , u'almuerzan' ],
[u'caer' , u'to fall; drop' , u'caigo' , u'caes' , u'cae' , u'caemos' , u'caéis' , u'caen' ],
[u'cerrar' , u'to close; shut' , u'cierro' , u'cierras' , u'cierra' , u'cerramos' , u'cerráis' , u'cierran' ],
[u'comenzar' , u'to begin; start' , u'comienzo' , u'comienzas' , u'comienza' , u'comenzamos' , u'comenzáis' , u'comienzan' ],
[u'conocer' , u'to be familiar' , u'conozco' , u'conoces' , u'conoce' , u'conocemos' , u'conocéis' , u'conocen' ],
[u'conseguir' , u'to get' , u'consigo' , u'consigues' , u'consigue' , u'conseguimos' , u'conseguís' , u'consiguen' ],
[u'contar' , u'to count; tell' , u'cuento' , u'cuentas' , u'cuenta' , u'contamos' , u'contáis' , u'cuentan' ],
[u'dar' , u'to give' , u'doy' , u'das' , u'da' , u'damos' , u'dais' , u'dan' ],
[u'decir' , u'to say; tell' , u'digo' , u'dices' , u'dice' , u'decimos' , u'decís' , u'dicen' ],
[u'defender' , u'to defend' , u'defiendo' , u'defiendes' , u'defiende' , u'defendemos' , u'defendéis' , u'defienden' ],
[u'dormir' , u'to sleep' , u'duermo' , u'duermes' , u'duerme' , u'dormimos' , u'dormís' , u'duermen' ],
[u'empezar' , u'to begin; start' , u'empiezo' , u'empiezas' , u'empieza' , u'empezamos' , u'empezáis' , u'empiezan' ],
[u'encontrar' , u'to find; meet' , u'encuentro' , u'encuentras' , u'encuentra' , u'encontramos' , u'encontráis' , u'encuentran' ],
[u'entender' , u'to understand' , u'entiendo' , u'entiendes' , u'entiende' , u'entendemos' , u'entendéis' , u'entienden' ],
[u'estar' , u'to be (temporary)' , u'estoy' , u'estás' , u'está' , u'estamos' , u'estáis' , u'están' ],
[u'haber' , u'to have; to credit' , u'he' , u'has' , u'ha' , u'hemos' , u'habéis' , u'han' ],
[u'hacer' , u'to do; make; perform' , u'hago' , u'haces' , u'hace' , u'hacemos' , u'hacéis' , u'hacen' ],
[u'ir' , u'to go' , u'voy' , u'vas' , u'va' , u'vamos' , u'vais' , u'van' ],
[u'jugar' , u'to play' , u'juego' , u'juegas' , u'juega' , u'jugamos' , u'jugáis' , u'juegan' ],
[u'llover' , u'to rain' , u'lluevo' , u'llueves' , u'llueve' , u'llovemos' , u'llovéis' , u'llueven' ],
[u'mostrar' , u'to show' , u'muestro' , u'muestras' , u'muestra' , u'mostramos' , u'mostráis' , u'muestran' ],
[u'mover' , u'to move' , u'muevo' , u'mueves' , u'mueve' , u'movemos' , u'movéis' , u'mueven' ],
[u'nevar' , u'to snow' , u'nievo' , u'nievas' , u'nieva' , u'nevamos' , u'neváis' , u'nievan' ],
[u'oir' , u'to hear' , u'oigo' , u'oyes' , u'oye' , u'oímos' , u'oís' , u'oyen' ],
[u'pedir' , u'to book; order; ask; reserve' , u'pido' , u'pides' , u'pide' , u'pedimos' , u'pedís' , u'piden' ],
[u'pensar' , u'to think' , u'pienso' , u'piensas' , u'piensa' , u'pensamos' , u'pensáis' , u'piensan' ],
[u'perder' , u'to lose; miss' , u'pierdo' , u'pierdes' , u'pierde' , u'perdemos' , u'perdéis' , u'pierden' ],
[u'poder' , u'to be able; can; may' , u'puedo' , u'puedes' , u'puede' , u'podemos' , u'podéis' , u'pueden' ],
[u'poner' , u'to put; put on; lay; send' , u'pongo' , u'pones' , u'pone' , u'ponemos' , u'ponéis' , u'ponen' ],
[u'querer' , u'to want; wish; like' , u'quiero' , u'quieres' , u'quiere' , u'queremos' , u'queréis' , u'quieren' ],
[u'recordar' , u'to remember; remind' , u'recuerdo' , u'recuerdas' , u'recuerda' , u'recordamos' , u'recordáis' , u'recuerdan' ],
[u'repetir' , u'to repeat' , u'repito' , u'repites' , u'repite' , u'repetimos' , u'repetís' , u'repiten' ],
[u'saber' , u'to know; know how' , u'sé' , u'sabes' , u'sabe' , u'sabemos' , u'sabéis' , u'saben' ],
[u'salir' , u'to exit; leave' , u'salgo' , u'sales' , u'sale' , u'salimos' , u'salís' , u'salen' ],
[u'seguir' , u'to follow' , u'sigo' , u'sigues' , u'sigue' , u'seguimos' , u'seguís' , u'siguen' ],
[u'sentir' , u'to feel' , u'siento' , u'sientes' , u'siente' , u'sentimos' , u'sentís' , u'sienten' ],
[u'ser' , u'to be (descriptive)' , u'soy' , u'eres' , u'es' , u'somos' , u'sois' , u'son' ],
[u'servir' , u'to serve' , u'sirvo' , u'sirves' , u'sirve' , u'servimos' , u'servís' , u'sirven' ],
[u'tener' , u'to have; own; keep' , u'tengo' , u'tienes' , u'tiene' , u'tenemos' , u'tenéis' , u'tienen' ],
[u'traer' , u'to bring; fetch' , u'traigo' , u'traes' , u'trae' , u'traemos' , u'traéis' , u'traen' ],
[u'venir' , u'to come' , u'vengo' , u'vienes' , u'viene' , u'venimos' , u'venís' , u'vienen' ],
[u'ver' , u'to see; view; look; consider' , u'veo' , u'ves' , u've' , u'vemos' , u'véis' , u'ven' ],
[u'volar' , u'to fly' , u'vuelo' , u'vuelas' , u'vuela' , u'volamos' , u'voláis' , u'vuelan' ],
[u'volver' , u'to return; go back' , u'vuelvo' , u'vuelves' , u'vuelve' , u'volvemos' , u'volvéis' , u'vuelven' ],
]
# -----------------------------------------
preterit_tense = [
[u'hablar' , u'to speak; talk' , u'hablé' , u'hablaste' , u'habló' , u'hablamos' , u'hablasteis' , u'hablaron' ],
[u'comer' , u'to eat; feed' , u'comí' , u'comiste' , u'comió' , u'comimos' , u'comisteis' , u'comieron' ],
[u'escrebir' , u'to write' , u'escrebí' , u'escrebiste' , u'escrebió' , u'escrebimos' , u'escrebisteis' , u'escrebieron' ],
[u'pagar' , u'to pay' , u'pagué' , u'pagaste' , u'pagó' , u'pagamos' , u'pagasteis' , u'pagaron' ],
[u'tocar' , u'to touch; play an instrument' , u'toqué' , u'tocaste' , u'tocó' , u'tocamos' , u'tocasteis' , u'tocaron' ],
[u'almorzar' , u'to (have) lunch' , u'almorcé' , u'almorzaste' , u'almorzó' , u'almorzamos' , u'almorzasteis' , u'almorzaron' ],
[u'caer' , u'to fall; drop' , u'caí' , u'caíste' , u'cayó' , u'caímos' , u'caísteis' , u'cayeron' ],
[u'cerrar' , u'to close; shut' , u'cerré' , u'cerraste' , u'cerró' , u'cerramos' , u'cerrasteis' , u'cerraron' ],
[u'comenzar' , u'to begin; start' , u'comencé' , u'comenzaste' , u'comenzó' , u'comenzamos' , u'comenzasteis' , u'comenzaron' ],
[u'conocer' , u'to be familiar' , u'conocí' , u'conociste' , u'conoció' , u'conocimos' , u'conocisteis' , u'conocieron' ],
[u'conseguir' , u'to get' , u'conseguí' , u'conseguiste' , u'consiguió' , u'conseguimos' , u'conseguisteis' , u'consiguieron' ],
[u'contar' , u'to count; tell' , u'conté' , u'contaste' , u'contó' , u'contamos' , u'contasteis' , u'contaron' ],
[u'dar' , u'to give' , u'di' , u'diste' , u'dio' , u'dimos' , u'disteis' , u'dieron' ],
[u'decir' , u'to say; tell' , u'dije' , u'dijiste' , u'dijo' , u'dijimos' , u'dijisteis' , u'dijeron' ],
[u'defender' , u'to defend' , u'defendí' , u'defendiste' , u'defendió' , u'defendimos' , u'defendisteis' , u'defendieron' ],
[u'dormir' , u'to sleep' , u'dormí' , u'dormiste' , u'durmío' , u'dormimos' , u'dormisteis' , u'durmieron' ],
[u'empezar' , u'to begin; start' , u'empecé' , u'empezaste' , u'empezó' , u'empezamos' , u'empezasteis' , u'empezaron' ],
[u'encontrar' , u'to find; meet' , u'encontré' , u'encontraste' , u'encontró' , u'encontramos' , u'encontrasteis' , u'encontraron' ],
[u'entender' , u'to understand' , u'entendí' , u'entendiste' , u'entendió' , u'entendimos' , u'entendisteis' , u'entendieron' ],
[u'estar' , u'to be (temporary)' , u'estuve' , u'estuviste' , u'estuvo' , u'estuvimos' , u'estuvisteis' , u'estuvieron' ],
[u'haber' , u'to have; to credit' , u'hube' , u'hubiste' , u'hubo' , u'hubimos' , u'hubisteis' , u'hubieron' ],
[u'hacer' , u'to do; make; perform' , u'hice' , u'hiciste' , u'hizo' , u'hicimos' , u'hicisteis' , u'hicieron' ],
[u'ir' , u'to go' , u'fui' , u'fuiste' , u'fue' , u'fuimos' , u'fuisteis' , u'fueron' ],
[u'jugar' , u'to play' , u'jugué' , u'jugaste' , u'jugó' , u'jugamos' , u'jugasteis' , u'jugaron' ],
[u'llover' , u'to rain' , u'lloví' , u'lloviste' , u'llovió' , u'llovimos' , u'llovisteis' , u'llovieron' ],
[u'mostrar' , u'to show' , u'mostré' , u'mostraste' , u'mostró' , u'mostramos' , u'mostrasteis' , u'mostraron' ],
[u'mover' , u'to move' , u'moví' , u'moviste' , u'movió' , u'movimos' , u'movisteis' , u'movieron' ],
[u'nevar' , u'to snow' , u'nevé' , u'nevaste' , u'nevó' , u'nevamos' , u'nevasteis' , u'nevaron' ],
[u'oir' , u'to hear' , u'oí' , u'oíste' , u'oyó' , u'oímos' , u'oísteis' , u'oyeron' ],
[u'pedir' , u'to book; order; ask; reserve' , u'pedí' , u'pediste' , u'pidió' , u'pedimos' , u'pedisteis' , u'pidieron' ],
[u'pensar' , u'to think' , u'pensé' , u'pensaste' , u'pensó' , u'pensamos' , u'pensasteis' , u'pensaron' ],
[u'perder' , u'to lose; miss' , u'perdí' , u'perdiste' , u'perdió' , u'perdimos' , u'perdisteis' , u'perdieron' ],
[u'poder' , u'to be able; can; may' , u'pude' , u'pudiste' , u'pudo' , u'pudimos' , u'pudisteis' , u'pudieron' ],
[u'poner' , u'to put; put on; lay; send' , u'puse' , u'pusiste' , u'puso' , u'pusimos' , u'pusisteis' , u'pusieron' ],
[u'querer' , u'to want; wish; like' , u'quise' , u'quisiste' , u'quiso' , u'quisimos' , u'quisisteis' , u'quisieron' ],
[u'recordar' , u'to remember; remind' , u'recordé' , u'recordaste' , u'recordó' , u'recordamos' , u'recordasteis' , u'recordaron' ],
[u'repetir' , u'to repeat' , u'repetí' , u'repetiste' , u'repitió' , u'repetimos' , u'repetisteis' , u'repitieron' ],
[u'saber' , u'to know; know how' , u'supe' , u'supiste' , u'supo' , u'supimos' , u'supisteis' , u'supieron' ],
[u'salir' , u'to exit; leave' , u'salí' , u'saliste' , u'salió' , u'salimos' , u'salisteis' , u'salieron' ],
[u'seguir' , u'to follow' , u'seguí' , u'seguiste' , u'siguió' , u'seguimos' , u'seguisteis' , u'siguieron' ],
[u'sentir' , u'to feel' , u'sentí' , u'sentiste' , u'sintió' , u'sentimos' , u'sentisteis' , u'sintieron' ],
[u'ser' , u'to be (descriptive)' , u'fui' , u'fuiste' , u'fue' , u'fuimos' , u'fuisteis' , u'fueron' ],
[u'servir' , u'to serve' , u'serví' , u'serviste' , u'sirvió' , u'servimos' , u'servisteis' , u'sirvieron' ],
[u'tener' , u'to have; own; keep' , u'tuve' , u'tuviste' , u'tuvo' , u'tuvimos' , u'tuvisteis' , u'tuvieron' ],
[u'traer' , u'to bring; fetch' , u'traje' , u'trajiste' , u'trajo' , u'trajimos' , u'trajisteis' , u'trajeron' ],
[u'venir' , u'to come' , u'vine' , u'viniste' , u'vinó' , u'vinimos' , u'vininsteis' , u'vinieron' ],
[u'ver' , u'to see; view; look; consider' , u'ví' , u'viste' , u'vió' , u'vimos' , u'visteis' , u'vieron' ],
[u'volar' , u'to fly' , u'volé' , u'volaste' , u'voló' , u'volamos' , u'volasteis' , u'volaron' ],
[u'volver' , u'to return; go back' , u'volví' , u'volviste' , u'volvió' , u'volvimos' , u'volvisteis' , u'volvieron' ],
]
# -----------------------------------------
imperfect_tense = [
[u'hablar' , u'to speak; talk' , u'hablaba' , u'hablabas' , u'hablaba' , u'hablábamos' , u'hablabais' , u'hablaban' ],
[u'comer' , u'to eat; feed' , u'comía' , u'comías' , u'comía' , u'comíamos' , u'comíais' , u'comían' ],
[u'escrebir' , u'to write' , u'escrebía' , u'escrebías' , u'escrebía' , u'escrebíamos' , u'escrebíais' , u'escrebían' ],
[u'pagar' , u'to pay' , u'pagaba' , u'pagabas' , u'pagaba' , u'pagábamos' , u'pagabais' , u'pagaban' ],
[u'tocar' , u'to touch; play an instrument' , u'tocaba' , u'tocabas' , u'tocaba' , u'tocábamos' , u'tocabais' , u'tocaban' ],
[u'almorzar' , u'to (have) lunch' , u'almorzaba' , u'almorzabas' , u'almorzaba' , u'almorzábamos' , u'almorzabais' , u'almorzaban' ],
[u'caer' , u'to fall; drop' , u'caía' , u'caías' , u'caía' , u'caíamos' , u'caíais' , u'caían' ],
[u'cerrar' , u'to close; shut' , u'cerraba' , u'cerrabas' , u'cerraba' , u'cerrábamos' , u'cerrabais' , u'cerraban' ],
[u'comenzar' , u'to begin; start' , u'comenzaba' , u'comenzabas' , u'comenzaba' , u'comenzábamos' , u'comenzabais' , u'comenzaban' ],
[u'conocer' , u'to be familiar' , u'conocía' , u'conocías' , u'conocía' , u'conocíamos' , u'conocíais' , u'conocían' ],
[u'conseguir' , u'to get' , u'conseguía' , u'conseguías' , u'conseguía' , u'conseguíamos' , u'conseguíais' , u'conseguían' ],
[u'contar' , u'to count; tell' , u'contaba' , u'contabas' , u'contaba' , u'contábamos' , u'contabais' , u'contaban' ],
[u'dar' , u'to give' , u'daba' , u'dabas' , u'daba' , u'dábamos' , u'dabais' , u'daban' ],
[u'decir' , u'to say; tell' , u'decía' , u'decías' , u'decía' , u'decíamos' , u'decíais' , u'decían' ],
[u'defender' , u'to defend' , u'defendía' , u'defendías' , u'defendía' , u'defendíamos' , u'defendíais' , u'defendían' ],
[u'dormir' , u'to sleep' , u'dormía' , u'dormías' , u'dormía' , u'dormíamos' , u'dormíais' , u'dormían' ],
[u'empezar' , u'to begin; start' , u'empezaba' , u'empezabas' , u'empezaba' , u'empezábamos' , u'empezabais' , u'empezaban' ],
[u'encontrar' , u'to find; meet' , u'encontraba' , u'encontrabas' , u'encontraba' , u'encontrábamos' , u'encontrabais' , u'encontraban' ],
[u'entender' , u'to understand' , u'entendía' , u'entendías' , u'entendía' , u'entendíamos' , u'entendíais' , u'entendían' ],
[u'estar' , u'to be (temporary)' , u'estaba' , u'estabas' , u'estaba' , u'estábamos' , u'estabais' , u'estaban' ],
[u'haber' , u'to have; to credit' , u'había' , u'habías' , u'había' , u'habíamos' , u'habíais' , u'habían' ],
[u'hacer' , u'to do; make; perform' , u'hacía' , u'hacías' , u'hacía' , u'hacíamos' , u'hacíais' , u'hacían' ],
[u'ir' , u'to go' , u'iba' , u'ibas' , u'iba' , u'íbamos' , u'ibais' , u'iban' ],
[u'jugar' , u'to play' , u'jugaba' , u'jugabas' , u'jugaba' , u'jugábamos' , u'jugabais' , u'jugaban' ],
[u'llover' , u'to rain' , u'llovía' , u'llovías' , u'llovía' , u'llovíamos' , u'llovíais' , u'llovían' ],
[u'mostrar' , u'to show' , u'mostraba' , u'mostrabas' , u'mostraba' , u'mostrábamos' , u'mostrabais' , u'mostraban' ],
[u'mover' , u'to move' , u'movía' , u'movías' , u'movía' , u'movíamos' , u'movíais' , u'movían' ],
[u'nevar' , u'to snow' , u'nevaba' , u'nevabas' , u'nevaba' , u'nevábamos' , u'nevabais' , u'nevaban' ],
[u'oir' , u'to hear' , u'oía' , u'oías' , u'oía' , u'oíamos' , u'oíais' , u'oían' ],
[u'pedir' , u'to book; order; ask; reserve' , u'pedía' , u'pedías' , u'pedía' , u'pedíamos' , u'pedíais' , u'pedían' ],
[u'pensar' , u'to think' , u'pensaba' , u'pensabas' , u'pensaba' , u'pensábamos' , u'pensabais' , u'pensaban' ],
[u'perder' , u'to lose; miss' , u'perdía' , u'perdías' , u'perdía' , u'perdíamos' , u'perdíais' , u'perdían' ],
[u'poder' , u'to be able; can; may' , u'podía' , u'podías' , u'podía' , u'podíamos' , u'podíais' , u'podían' ],
[u'poner' , u'to put; put on; lay; send' , u'ponía' , u'ponías' , u'ponía' , u'poníamos' , u'poníais' , u'ponían' ],
[u'querer' , u'to want; wish; like' , u'quería' , u'querías' , u'quería' , u'queríamos' , u'queríais' , u'querían' ],
[u'recordar' , u'to remember; remind' , u'recordaba' , u'recordabas' , u'recordaba' , u'recordábamos' , u'recordabais' , u'recordaban' ],
[u'repetir' , u'to repeat' , u'repetía' , u'repetías' , u'repetía' , u'repetíamos' , u'repetíais' , u'repetían' ],
[u'saber' , u'to know; know how' , u'sabía' , u'sabías' , u'sabía' , u'sabíamos' , u'sabíais' , u'sabían' ],
[u'salir' , u'to exit; leave' , u'salía' , u'salías' , u'salía' , u'salíamos' , u'salíais' , u'salían' ],
[u'seguir' , u'to follow' , u'seguía' , u'seguías' , u'seguía' , u'seguíamos' , u'seguíais' , u'seguían' ],
[u'sentir' , u'to feel' , u'sentía' , u'sentías' , u'sentía' , u'sentíamos' , u'sentíais' , u'sentían' ],
[u'ser' , u'to be (descriptive)' , u'era' , u'eras' , u'era' , u'éramos' , u'erais' , u'eran' ],
[u'servir' , u'to serve' , u'servía' , u'servías' , u'servía' , u'servíamos' , u'servíais' , u'servían' ],
[u'tener' , u'to have; own; keep' , u'tenía' , u'tenías' , u'tenía' , u'teníamos' , u'teníais' , u'tenían' ],
[u'traer' , u'to bring; fetch' , u'traía' , u'traías' , u'traía' , u'traíamos' , u'traíais' , u'traían' ],
[u'venir' , u'to come' , u'venía' , u'venías' , u'venía' , u'veníamos' , u'veníais' , u'venían' ],
[u'ver' , u'to see; view; look; consider' , u'veía' , u'veías' , u'veía' , u'veíamos' , u'veíais' , u'veían' ],
[u'volar' , u'to fly' , u'volaba' , u'volabas' , u'volaba' , u'volábamos' , u'volabais' , u'volaban' ],
[u'volver' , u'to return; go back' , u'volvía' , u'volvías' , u'volvía' , u'volvíamos' , u'volvíais' , u'volvían' ],
]
# -----------------------------------------
future_tense = [
[u'hablar' , u'to speak; talk' , u'hablaré' , u'hablarás' , u'hablará' , u'hablaremos' , u'hablaréis' , u'hablarán' ],
[u'comer' , u'to eat; feed' , u'comeré' , u'comerás' , u'comerá' , u'comeremos' , u'comeréis' , u'comerán' ],
[u'escrebir' , u'to write' , u'escrebiré' , u'escrebirás' , u'escrebirá' , u'escrebiremos' , u'escrebiréis' , u'escrebirán' ],
[u'pagar' , u'to pay' , u'pagaré' , u'pagarás' , u'pagará' , u'pagaremos' , u'pagaréis' , u'pagarán' ],
[u'tocar' , u'to touch; play an instrument' , u'tocaré' , u'tocarás' , u'tocará' , u'tocaremos' , u'tocaréis' , u'tocarán' ],
[u'almorzar' , u'to (have) lunch' , u'almorzaré' , u'almorzarás' , u'almorzará' , u'almorzaremos' , u'almorzaréis' , u'almorzarán' ],
[u'caer' , u'to fall; drop' , u'caeré' , u'caerás' , u'caerá' , u'caeremos' , u'caeréis' , u'caerán' ],
[u'cerrar' , u'to close; shut' , u'cerraré' , u'cerrarás' , u'cerrará' , u'cerraremos' , u'cerraréis' , u'cerrarán' ],
[u'comenzar' , u'to begin; start' , u'comenzaré' , u'comenzarás' , u'comenzará' , u'comenzaremos' , u'comenzaréis' , u'comenzarán' ],
[u'conocer' , u'to be familiar' , u'conoceré' , u'conocerás' , u'conocerá' , u'conoceremos' , u'conoceréis' , u'conocerán' ],
[u'conseguir' , u'to get' , u'consiguiere' , u'consiguieres' , u'consiguiere' , u'consiguiéremos' , u'consiguiereis' , u'consiguieren' ],
[u'contar' , u'to count; tell' , u'contaré' , u'contarás' , u'contará' , u'contaremos' , u'contaréis' , u'contarán' ],
[u'dar' , u'to give' , u'daré' , u'darás' , u'dará' , u'daremos' , u'daréis' , u'darán' ],
[u'decir' , u'to say; tell' , u'diré' , u'dirás' , u'dirá' , u'diremos' , u'diréis' , u'dirán' ],
[u'defender' , u'to defend' , u'defenderé' , u'defenderás' , u'defenderá' , u'defenderemos' , u'defenderéis' , u'defenderán' ],
[u'dormir' , u'to sleep' , u'dormiré' , u'dormirás' , u'dormirá' , u'dormiremos' , u'dormiréis' , u'dormirán' ],
[u'empezar' , u'to begin; start' , u'empezaré' , u'empezarás' , u'empezará' , u'empezaremos' , u'empezaréis' , u'empezarán' ],
[u'encontrar' , u'to find; meet' , u'encontraré' , u'encontrarás' , u'encontrará' , u'encontraremos' , u'encontraréis' , u'encontrarán' ],
[u'entender' , u'to understand' , u'entenderé' , u'entenderás' , u'entenderá' , u'entenderemos' , u'entenderéis' , u'entenderán' ],
[u'estar' , u'to be (temporary)' , u'estaré' , u'estarás' , u'estará' , u'estaremos' , u'estaréis' , u'estarán' ],
[u'haber' , u'to have; to credit' , u'habré' , u'habrás' , u'habrá' , u'habremos' , u'habréis' , u'habrán' ],
[u'hacer' , u'to do; make; perform' , u'haré' , u'harás' , u'hará' , u'haremos' , u'haréis' , u'harán' ],
[u'ir' , u'to go' , u'iré' , u'irás' , u'irá' , u'iremos' , u'iréis' , u'irán' ],
[u'jugar' , u'to play' , u'jugaré' , u'jugarás' , u'jugará' , u'jugaremos' , u'jugaréis' , u'jugarán' ],
[u'llover' , u'to rain' , u'lloveré' , u'lloverás' , u'lloverá' , u'lloveremos' , u'lloveréis' , u'lloverán' ],
[u'mostrar' , u'to show' , u'mostraré' , u'mostrarás' , u'mostrará' , u'mostraremos' , u'mostraréis' , u'mostrarán' ],
[u'mover' , u'to move' , u'moveré' , u'moverás' , u'moverá' , u'moveremos' , u'moveréis' , u'moverán' ],
[u'nevar' , u'to snow' , u'nevaré' , u'nevarás' , u'nevará' , u'nevaremos' , u'nevaréis' , u'nevarán' ],
[u'oir' , u'to hear' , u'oiré' , u'oirás' , u'oirá' , u'oiremos' , u'oiréis' , u'oirán' ],
[u'pedir' , u'to book; order; ask; reserve' , u'pediré' , u'pedirás' , u'pedirá' , u'pediremos' , u'pediréis' , u'pedirán' ],
[u'pensar' , u'to think' , u'pensaré' , u'pensarás' , u'pensará' , u'pensaremos' , u'pensaréis' , u'pensarán' ],
[u'perder' , u'to lose; miss' , u'perderé' , u'perderás' , u'perderá' , u'perderemos' , u'perderéis' , u'perderán' ],
[u'poder' , u'to be able; can; may' , u'podré' , u'podrás' , u'podrá' , u'podremos' , u'podréis' , u'podrán' ],
[u'poner' , u'to put; put on; lay; send' , u'pondré' , u'pondrás' , u'pondrá' , u'pondremos' , u'pondréis' , u'pondrán' ],
[u'querer' , u'to want; wish; like' , u'querré' , u'querrás' , u'querrá' , u'querremos' , u'querréis' , u'querrán' ],
[u'recordar' , u'to remember; remind' , u'recordaré' , u'recordarás' , u'recordará' , u'recordaremos' , u'recordaréis' , u'recordarán' ],
[u'repetir' , u'to repeat' , u'repetiré' , u'repetirás' , u'repetirá' , u'repetiremos' , u'repetiréis' , u'repetirán' ],
[u'saber' , u'to know; know how' , u'sabré' , u'sabrás' , u'sabrá' , u'sabremos' , u'sabréis' , u'sabrán' ],
[u'salir' , u'to exit; leave' , u'saldré' , u'saldrás' , u'saldrá' , u'saldremos' , u'saldréis' , u'saldrán' ],
[u'seguir' , u'to follow' , u'seguiré' , u'seguirás' , u'seguirá' , u'seguiremos' , u'seguiréis' , u'seguirán' ],
[u'sentir' , u'to feel' , u'sentiré' , u'sentirás' , u'sentirá' , u'sentiremos' , u'sentiréis' , u'sentirán' ],
[u'ser' , u'to be (descriptive)' , u'seré' , u'serás' , u'será' , u'seremos' , u'seréis' , u'serán' ],
[u'servir' , u'to serve' , u'serviré' , u'servirás' , u'servirá' , u'serviremos' , u'serviréis' , u'servirán' ],
[u'tener' , u'to have; own; keep' , u'tendré' , u'tendrás' , u'tendrá' , u'tendremos' , u'tendréis' , u'tendrán' ],
[u'traer' , u'to bring; fetch' , u'traeré' , u'traerás' , u'traerá' , u'traeremos' , u'traeréis' , u'traerán' ],
[u'venir' , u'to come' , u'vendré' , u'vendrás' , u'vendrá' , u'vendremos' , u'vendréis' , u'vendrán' ],
[u'ver' , u'to see; view; look; consider' , u'veré' , u'verás' , u'verá' , u'veremos' , u'veréis' , u'verán' ],
[u'volar' , u'to fly' , u'volaré' , u'volarás' , u'volará' , u'volaremos' , u'volaréis' , u'volarán' ],
[u'volver' , u'to return; go back' , u'volveré' , u'volverás' , u'volverá' , u'volveremos' , u'volveréis' , u'volverán' ],
]
