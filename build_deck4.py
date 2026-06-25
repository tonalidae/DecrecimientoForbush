# -*- coding: utf-8 -*-
import json
I = json.load(open('figs_hd.json'))

def img(key, cap=None, cls=""):
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="{cls}"><img src="{I[key]}">{c}</figure>'

def note(t):
    return '<aside class="notes">' + t + '</aside>'

def divider(num, title, subtitle, n):
    return ('<section class="divider" data-background-gradient="linear-gradient(135deg,#0b1f3a,#123a63)">'
      f'<div class="dlabel">{num}</div><h1 class="dtitle">{title}</h1>'
      f'<p class="dsub">{subtitle}</p>' + note(n) + '</section>')

slides = []

# ---------- PORTADA ----------
slides.append('<section data-background-gradient="radial-gradient(1200px 700px at 75% -10%, rgba(63,169,245,.30), transparent), linear-gradient(160deg,#0a1526,#0d1b30)">'
  '<div class="reto">RETO 14 · EQUIPO 1 — DÍAS DE TORMENTA</div>'
  '<h1 class="maintitle">Muones, magnetómetros y transitorios cósmicos</h1>'
  '<p class="lead">Decrecimiento Forbush, pulsaciones geomagnéticas y modulación de rayos cósmicos durante la tormenta geomagnética del 19–21 de enero de 2026</p>'
  '<table class="team">'
  '<tr><td>Andre Jared Aguilar Ochoa</td><td>Honduras</td></tr>'
  '<tr><td>Stephanie Carolina Cely Rodríguez</td><td>Colombia</td></tr>'
  '<tr><td>Peter Armando Perez Antaurco</td><td>Perú</td></tr>'
  
  '</table>'
  '<p class="datebadge">Junio de 2026</p>'
  + note("Buenas. Somos el Equipo 1 y defendemos la parte de DÍAS DE TORMENTA del Reto 14: el decrecimiento Forbush y la respuesta geomagnética durante la tormenta del 19 al 21 de enero de 2026. Somos seis integrantes de Honduras, Colombia, Perú, El Salvador y Guatemala. Cada uno expondrá una parte y podrá responder sobre su aporte. [REPARTO sugerido: Aguilar—problema/enfoque; Tojil—física; Perez—MuNRA; Coloma—metodología; Cely—resultados MuNRA/EZIE; Jovel—resultados globales y conclusiones.]")
  + '</section>')

# ========== 1. FORMA DE ABORDAR EL PROBLEMA ==========
slides.append([
 divider("1 · FORMA DE ABORDAR EL PROBLEMA","Forma de abordar el problema","","Objetivo, enfoque multi-instrumental e hipótesis de trabajo."),
 '<section><ul>'
 '<li class="fragment"><b>Objetivo:</b> caracterizar el <b>decrecimiento Forbush</b> y la respuesta geomagnética durante la <b>tormenta del 19–21 ene 2026</b>.</li>'
 '<li class="fragment"><b>Análisis multi-instrumental:</b> combinar análisis de rayos cósmicos (muones y neutrones), campo geomagnético y viento solar para ordenar la cadena causal del evento.</li>'
 '<li class="fragment"><b>Hipótesis:</b> la depresión de rayos cósmicos y la depresión del campo son respuestas acopladas a la CME.</li>'
 '</ul>'
 + note("El objetivo de nuestro equipo es caracterizar el decrecimiento Forbush y la respuesta geomagnética durante la tormenta del 19 al 21 de enero de 2026. La estrategia fue multi-instrumental: cruzar rayos cósmicos, campo magnético y viento solar para ordenar la secuencia causal. La hipótesis de trabajo es que la caída de rayos cósmicos y la depresión del campo son dos caras del mismo forzamiento: la CME.")
 + '</section>',
 '<section>'
 '<div class="card accentA fragment"><h3>Forbush</h3><p>La CME barre los rayos cósmicos de menor rigidez (Magnetosheath + nube magnética) → caída del flujo 1–3 días después.</p></div>'
 '<p class="fragment">Tres fases: <b>SSC</b> → <b>fase principal</b> (\\(B_z<0\\), corriente anular) → <b>recuperación</b>. Intensidad por \\(D_{st}\\): extrema \\(<-200\\) nT.</p>'
 '<p class="callout fragment">Evento: CME asociada a la llamarada X1.95 · <b>Kp ≈ 8 (G4)</b> · \\(D_{st,\\text{mín}} = -236\\) nT (extrema).</p>'
 + note(" la llamarada y la CME NO son lo mismo. La llamarada X1.95 del 18 de enero es radiación: llega en minutos y afecta la ionosfera, pero no deprime el campo geomagnético. Lo que causó la tormenta fue la CME asociada, el plasma magnetizado. El decrecimiento Forbush ocurre porque esa CME —su vaina turbulenta y su nube magnética— barre los rayos cósmicos de menor rigidez. La tormenta tiene tres fases: inicio súbito, fase principal con Bz al sur que forma la corriente anular, y recuperación. Nuestro evento alcanzó Kp cercano a 8, nivel G4, y un Dst mínimo de menos 236, categoría extrema.")
 + '</section>',
])

# ========== 2. ¿CÓMO SE HIZO? ==========
slides.append([
 divider("2 · ¿CÓMO SE HIZO?","Instrumentos, calibración del MuNRA y metodología","","Instrumentos usados, pipeline de calibración del MuNRA y metodología de correlación."),
 '<section><h2>Instrumentos y datos</h2><div class="grid2"><div><ul class="tight">'
 '<li><b>MuNRA</b> — muones, Tegucigalpa, Honduras (14,1°N · 60 s)</li>'
 '<li><b>EZIE-Mag / MAGHO-1</b> — campo, Honduras (14,1°N · 60 s)</li>'
 '<li><b>COE-COENEO</b> — campo de referencia, México (19,8°N · INTERMAGNET)</li>'
 '<li><b>NMDB</b> — neutrones: MXCO 19,3°N · NEWK 40,0°N · CALG 51,1°N (1 h)</li>'
 '<li><b>OMNIWeb</b> — viento solar / IMF en L1 (1 h)</li></ul>'
 '<p class="callout">Períodos: P1 (9–16 ene, base) y P2 (18–23 ene, tormenta).</p></div>'
 + img('map','Cobertura geográfica: MuNRA/EZIE-Mag (14,1°N), COE-COENEO (19,8°N), NMDB MXCO (19,3°N) · NEWK (40,0°N) · CALG (51,1°N).') + '</div>'
 + note("Usamos cinco instrumentos. El detector de muones MuNRA en Tegucigalpa y los monitores de neutrones NMDB miden los rayos cósmicos. El magnetómetro EZIE-Mag en Honduras y el observatorio Coeneo en México miden el campo. Y OMNIWeb nos da el viento solar en L1. Definimos dos períodos: P1 antes de la tormenta, para la línea base, y P2 durante la tormenta. A la derecha, la línea base estable del MuNRA antes del evento.")
 + '</section>',
 '<section><h2>Calibración del MuNRA</h2><div class="grid2"><div><ul class="tight">'
 '<li><b>Discretización</b> en intervalos de 60 s + corrección por <b>tiempo vivo</b> (tiempo muerto ≈ 10 %).</li>'
 '<li>Modelo ambiental \\(R=\\mu_R+\\beta\\,\\Delta P+\\alpha\\,\\Delta T\\); \\(\\alpha,\\beta\\) por <b>regresión múltiple</b> (Cramer) para romper la multicolinealidad P–T.</li>'
 '<li>Resultado base: <b>4,389 ± 0,295 cuentas s⁻¹</b>.</li></ul></div>'
 '<div class="card accentA"><h3>Coeficientes</h3><p>\\(\\beta=-6{,}05\\times10^{-5}\\) (cuentas s⁻¹)/Pa<br>\\(\\alpha=-0{,}0487\\) (cuentas s⁻¹)/°C<br>Constantes, aplicados a la serie de tormenta.</p></div></div>'
 + img('munra_cont','MuNRA — línea base estable (1–12 ene): ≈ 4,5 cuentas s⁻¹.')
 + note("Sobre el MuNRA hicimos un pipeline de calibración propio. Primero, discretizamos los eventos en intervalos de 60 segundos y corregimos por tiempo vivo, porque el detector tiene un tiempo muerto cercano al 10 % que, de no corregirse, subestimaría el flujo. Segundo, modelamos los efectos ambientales: presión y temperatura. Como en Tegucigalpa presión y temperatura están muy correlacionadas, una covarianza simple da signos erróneos; por eso usamos regresión múltiple resuelta por la regla de Cramer para desacoplar los coeficientes. Obtuvimos una tasa base de 4,39 cuentas por segundo y coeficientes barométrico y térmico negativos, que aplicamos como constantes a la serie de la tormenta.")
 + '</section>',
 '<section><h2>Metodología de correlación</h2><ul>'
 '<li class="fragment"><b>Sincronización</b> de instrumentos por vecino más cercano (\\(\\delta t=5\\) min); brechas como NaN, sin interpolar.</li>'
 '<li class="fragment"><b>Pearson diaria + transformada de Fisher</b> (umbral \\(|r|\\ge0{,}403\\)).</li>'
 '<li class="fragment"><b>Correlación cruzada con retardo</b> \\(\\tau^*=\\arg\\max|C_{XY}(\\tau)|\\) → adelantos/atrasos entre señales.</li>'
 '<li class="fragment"><b>Correlación móvil</b> (ventanas 12–24 h) para seguir el acoplamiento fase a fase.</li></ul>'
 + note("Para la metodología de correlación: sincronizamos todos los instrumentos por vecino más cercano con tolerancia de 5 minutos, y dejamos las brechas como huecos, sin inventar datos. Calculamos correlaciones de Pearson diarias estabilizadas con la transformada de Fisher. Usamos correlación cruzada con retardo para ver qué señal adelanta a cuál, y correlación móvil con ventanas de 12 a 24 horas para seguir el acoplamiento a lo largo de las fases de la tormenta.")
 + '</section>',
])

# ========== 3. RESULTADOS ==========
slides.append([
 divider("3 · RESULTADOS","Resultados","","MuNRA, acoplamiento EZIE-Mag, evolución global de la tormenta y Forbush en neutrones."),
 '<section><h2>MuNRA durante la tormenta</h2><div class="grid2">'
 + img('munra_geo','MuNRA 19–26 ene: caída del flujo y vacío de adquisición.') +
 '<div><ul class="tight"><li>Caída brusca del flujo de muones con el inicio de la tormenta.</li>'
 '<li><b>Vacío de 42,68 h</b>: la caída del campo (~13:00 UTC) coincide con la desconexión serial (~13:06 UTC).</li>'
 '<li>Atribuido a saturación del búfer por corrientes inducidas por la CME.</li></ul></div></div>'
 + note("Primer resultado, el MuNRA durante la tormenta. Se ve la caída del flujo de muones al iniciar el evento. Pero también un vacío de adquisición de casi 43 horas: la caída del campo magnético a las 13:00 coincide al minuto con la desconexión del detector a las 13:06. Lo atribuimos a una saturación del búfer por las corrientes que induce la CME. Es una limitación que reconocemos: con el MuNRA no pudimos cubrir el mínimo del Forbush, y por eso nos apoyamos en los neutrones.")
 + '</section>',
 '<section><h2>Acoplamiento EZIE-Mag ↔ MuNRA</h2><div class="grid2">'
 + img('corr_ezie_munra','Correlación móvil tasa de muones vs campo horizontal.')
 + img('scatter','COE vs EZIE-Mag: r = 0,968 (estaciones a ≈ 620 km).') + '</div>'
 '<p class="callout">Con ventanas de 12–24 h emerge \\(r>0{,}6\\): la recuperación del campo y la del flujo son la misma respuesta física.</p>'
 + note("Segundo, el acoplamiento entre el campo y los muones. Con la correlación móvil, ventanas cortas dan ruido, pero al ampliar a 12–24 horas aparece una correlación mayor que 0,6 en la recuperación: el restablecimiento del campo y el del flujo de rayos cósmicos son la misma respuesta. Y entre los dos magnetómetros, Honduras y México, la correlación es de 0,97 con desfase cero, pese a 620 km de separación: la perturbación fue coherente a gran escala.")
 + '</section>',
 '<section><h2>Evolución global de la tormenta</h2><div class="grid2">'
 + img('omniweb','Muones, Dst, Kp, campo y parámetros OMNIWeb (18–27 ene).') +
 '<div><ul class="tight"><li><b>SSC</b> ≈ 16:00 UT 19 ene.</li>'
 '<li><b>Fase principal</b>: Dst ≈ −230 nT, Kp > 8.</li>'
 '<li>\\(V_{sw}>1000\\) km/s; \\(\\text{IMF}\\,B_z<0\\) (reconexión).</li>'
 '<li>Recuperación de varios días.</li></ul></div></div>'
 + note("Tercero, la visión global. El inicio súbito hacia las 16 UT del 19 de enero; la fase principal lleva el Dst a menos 230 y el Kp por encima de 8; coincide con viento solar de más de 1000 km/s y campo interplanetario al sur, que habilita la reconexión. La recuperación dura varios días. Todo encaja con la llegada de la CME.")
 + '</section>',
 '<section><div class="grid2">'
 + img('forbush','Dst vs NMDB-México y fases de la respuesta.') +
 '<div><table class="mini"><tr><th></th><th>MXCO</th><th>NEWK</th><th>CALG</th></tr>'
 '<tr><td>Latitud</td><td>19,3°N</td><td>40,0°N</td><td>51,1°N</td></tr>'
 '<tr><td>Profundidad</td><td>−16,7%</td><td>−20,4%</td><td>−22,2%</td></tr></table>'
 '<p style="font-size:.8em">Más profundo a mayor latitud; recuperación > 4 días.</p>'
 '<ul class="tight"><li>\\(V_{sw}\\): <b>r=−0,86</b> · \\(D_{st}\\): <b>0,83</b></li>'
 '<li>Retardos ≈ 0 h → respuesta casi simultánea.</li></ul></div></div>'
 + note("Cuarto, el Forbush en los neutrones, que sí cubren el mínimo. Las tres estaciones marcan decrecimientos bien definidos, más profundos a mayor latitud: 16,7 % en México, 20,4 en Newark, 22,2 en Calgary. ¿Qué lo controla? La matriz de correlación señala la velocidad del viento solar, menos 0,86, y el Dst, 0,83, como los factores dominantes. Y los retardos son cercanos a cero: la respuesta es casi simultánea a la perturbación interplanetaria.")
 + '</section>',
])

# ========== 4. QUÉ ENTREGAMOS ==========
# slides.append([
#  divider("4 · ¿QUÉ ENTREGAMOS?","Entregables del equipo","",
#    "Breve: qué productos entregamos."),
#  '<section><h2>Entregables</h2><ul>'
#  '<li class="fragment"><b>Informe científico</b> del evento de tormenta (con correcciones de física y figuras).</li>'
#  '<li class="fragment"><b>Pipeline de calibración del MuNRA</b> en Python: tiempo vivo, corrección barométrica/térmica y serie en cuentas s⁻¹.</li>'
#  '<li class="fragment"><b>Series sincronizadas y análisis de correlación</b> (Fisher, cruzada con retardo, móvil) entre MuNRA, EZIE-Mag, NMDB y OMNIWeb.</li>'
#  '<li class="fragment"><b>Figuras y tablas</b>: caracterización del MuNRA, acoplamiento campo–muones, evolución de la tormenta y matriz de correlaciones.</li></ul>'
#  + note("¿Qué entregamos? Un informe científico del evento de tormenta, ya con las correcciones de física. Un pipeline de calibración del MuNRA en Python, que convierte los eventos crudos en una serie corregida en cuentas por segundo. Las series sincronizadas y todo el análisis de correlación entre los cuatro instrumentos. Y el conjunto de figuras y tablas que sustentan los resultados.")
#  + '</section>',
# ])

# ========== 5. CONCLUSIONES ==========
slides.append([
 divider("5 · CONCLUSIONES","Conclusiones","","Limitaciones del MuNRA, verificación con NMDB, correlaciones geomagnéticas, retardos temporales y trabajo a futuro."),

 # --- 5a. MuNRA: logros y limitaciones ---
 '<section><h2>Limitaciones del MuNRA</h2><div class="grid2"><div><ul class="tight">'
 '<li class="fragment"><b>Tasa basal estable:</b> 4,39 ± 0,29 Hz (≈ 263 muones/min) — detector calibrado y en operación.</li>'
 '<li class="fragment"><b>Tiempo muerto 10,07 %</b>: corrección obligatoria; sin ella el flujo se subestimaría sistemáticamente.</li>'
 '<li class="fragment"><b>Vacío de 42,68 h</b>: la caída del campo a las 13:00 UTC coincide al minuto con la desconexión serial (13:06 UTC) → saturación inducida por la CME.</li>'
 '<li class="fragment"><b>Muestra estadísticamente pequeña</b> (248 h ≈ 10 días): no es suficiente para conclusiones definitivas sobre el Forbush; se necesitan más datos.</li>'
 '</ul></div>'
 '<div class="card accentA fragment"><h3>¿Dónde se verifica?</h3>'
 '<p>La caída del flujo se confirma con los monitores de <b>neutrones NMDB</b>, que sí mantuvieron registro continuo durante toda la tormenta.</p>'
 '</div></div>'
 + note("El MuNRA es nuestro instrumento propio. Lo calibramos, lo corregimos por tiempo muerto y por efectos ambientales, y obtenemos una tasa basal estable. Pero tiene un límite importante: durante la tormenta se desconectó por 42 horas seguidas, justo cuando ocurrió el mínimo del Forbush. Y aunque vemos la caída antes y la recuperación después, el registro de 10 días es estadísticamente pequeño para sacar conclusiones definitivas. Por eso la verificación del decrecimiento Forbush la hacemos con los monitores de neutrones NMDB, que no se interrumpieron.")
 + '</section>',

 # --- 5b. NMDB y correlación campo-rayos cósmicos ---
 '<section><h2>Verificación con NMDB y correlaciones</h2>'
 '<div class="grid2"><div><ul class="tight">'
 '<li class="fragment"><b>Forbush en tres estaciones NMDB</b>: gradiente latitudinal claro — más profundo a mayor latitud (19°→40°→51°N).</li>'
 '<li class="fragment"><b>EZIE-Mag ↔ MuNRA</b> (ventanas 12–24 h): \\(r > 0{,}6\\) en la recuperación → campo y flujo de rayos cósmicos son respuestas acopladas a la misma CME.</li>'
 '<li class="fragment"><b>TEO–NMDB a escala de un año (2025):</b> \\(r = 0{,}497\\) — correlación moderada, significativa pero no fuerte.</li>'
 '<li class="fragment">A escala de <b>ciclo solar completo (11 años)</b> se espera una <b>anticorrelación</b>: con solo un año de datos no es posible observar ese patrón aún.</li>'
 '</ul></div>'
 '<div><table class="mini">'
 '<tr><th></th><th>MXCO</th><th>NEWK</th><th>CALG</th></tr>'
 '<tr><td>Lat.</td><td>19,3°N</td><td>40,0°N</td><td>51,1°N</td></tr>'
 '<tr><td>Caída</td><td>−16,7 %</td><td>−20,4 %</td><td>−22,2 %</td></tr>'
 '</table>'
 '<p class="callout" style="margin-top:.8em">\\(r_{V_{sw}}=-0{,}86\\) · \\(r_{D_{st}}=0{,}83\\) · \\(r_{B_{total}}=-0{,}76\\)</p>'
 '</div></div>'
 + note("Los monitores de neutrones nos dan la imagen completa del Forbush. Las tres estaciones muestran decrecimientos bien definidos, y la profundidad aumenta con la latitud porque el blindaje geomagnético es menor en latitudes altas. La correlación entre el magnetómetro EZIE-Mag y el MuNRA emerge solo al ampliar las ventanas temporales a 12 o 24 horas, lo que tiene sentido físico: el ruido de Poisson del MuNRA domina a corto plazo, pero la tendencia macroscópica revela el acoplamiento. Y sobre la correlación TEO-NMDB en días calmos: es moderada en un año, pero la anticorrelación real entre rayos cósmicos y actividad solar solo se ve en la escala de un ciclo solar de 11 años.")
 + '</section>',

 # --- 5c. Retardos temporales: interpretación física ---
 '<section><h2>Retardos temporales: ¿por qué ocurren?</h2><ul>'
 '<li class="fragment"><b>Lag ≈ 0 h en \\(V_{sw}\\) y \\(D_{st}\\)</b>: la disminución de rayos cósmicos y la depresión geomagnética son <em>simultáneas</em> → la CME actúa como barrera inmediata al llegar a la Tierra.</li>'
 '<li class="fragment"><b>Lag = −7 h en \\(\\text{IMF}\\,B_z\\)</b>: \\(B_z\\) es la única variable que <em>anticipa</em> el evento — es el gatillo de la reconexión magnética que abre la magnetosfera antes de que llegue el plasma de la CME.</li>'
 '<li class="fragment"><b>Lag = 1 h en \\(B_{total}\\), 3 h en densidad</b>: reflejan la estructura secuencial interna de la CME — primero la vaina turbulenta (campo), luego la nube magnética densa.</li>'
 '<li class="fragment">En conjunto, los retardos trazan la <b>cadena causal</b>: \\(B_z \\to\\) reconexión \\(\\to\\) tormenta + barrera para rayos cósmicos.</li>'
 '</ul>'
 + note("Este es uno de los resultados más ricos del análisis. Los retardos cero en velocidad del viento solar y en Dst nos dicen que la disminución de rayos cósmicos y la tormenta geomagnética ocurren juntas, sin retraso medible a resolución horaria. Pero el IMF Bz, el campo interplanetario norte-sur, anticipa el evento en 7 horas porque es el parámetro que controla la reconexión magnética: cuando Bz se vuelve al sur, la magnetosfera se abre, y eso prepara el camino para la tormenta y para la entrada de la CME. Los retardos en Btotal y densidad reflejan que la CME no es uniforme: primero llega la vaina turbulenta, con campo elevado, y después la nube magnética, más densa. Los retardos nos cuentan la secuencia interna de la estructura interplanetaria.")
 + '</section>',

 # --- 5d. Red geomagnética regional ---
 '<section><h2>Red geomagnética regional</h2><div class="grid2"><div><ul class="tight">'
 '<li class="fragment"><b>COE (México, 19,8°N) ↔ EZIE-Mag (Honduras, 14,1°N)</b>: \\(r = 0{,}968\\), lag \\(\\tau^*=0\\) h — coherencia a gran escala pese a 620 km de separación.</li>'
 '<li class="fragment">Desde 2026 Honduras tiene registro continuo del magnetómetro; muestra <b>mejor correlación con México que con Puerto Rico</b>.</li>'
 '<li class="fragment">Puerto Rico es una isla más influenciada por los campos magnéticos del océano y su posición geográfica introduce un comportamiento diferente.</li>'
 '<li class="fragment">El <b>campo magnético terrestre no es simétrico ni uniforme</b>: México y Honduras comparten un patrón regional similar, lo que valida usar COE como referencia continental para EZIE-Mag.</li>'
 '</ul></div>'
 + img('scatter','COE vs EZIE-Mag: r = 0,968 — coherencia regional a escala de tormenta.')
 + '</div>'
 + note("La alta correlación entre los dos magnetómetros, México y Honduras, es un resultado importante en sí mismo. Nos dice que la perturbación geomagnética fue coherente a escala regional, no local. Y el hecho de que Honduras correlacione mejor con México que con Puerto Rico tiene una explicación física: el campo magnético terrestre no es uniforme. Puerto Rico, al ser una isla, está más influenciada por los campos magnéticos del océano, que actúan como un conductor que distorsiona la señal. México y Honduras, siendo continentales y cercanos en longitud, comparten un patrón de campo regional más similar.")
 + '</section>',

 # --- 5e. Trabajo a futuro ---
 '<section data-background-gradient="linear-gradient(135deg,#0b1f3a,#123a63)">'
 '<div class="dlabel" style="font-size:.9em">TRABAJO A FUTURO</div>'
 '<ul style="margin-top:1.2em;font-size:.78em;line-height:1.7">'
 '<li class="fragment">Ampliar el <b>registro temporal del MuNRA</b> (ya calibrado y en operación) para obtener muestras estadísticamente significativas del Forbush.</li>'
 '<li class="fragment">Desplegar los <b>otros detectores MuNRA adquiridos en distintos países</b> → construir una red multi-punto y comparar decrecimientos entre sí.</li>'
 '<li class="fragment">Comparar la <b>red MuNRA con datos NMDB</b> para validar que los muones capturan los mismos decrecimientos que los neutrones.</li>'
 '<li class="fragment">Para correlaciones con <b>campo magnético</b>: enfocarse en períodos de tormenta — en días calmos la correlación es débil; el acoplamiento solo es significativo durante eventos extremos.</li>'
 '<li class="fragment">Estudiar la <b>anticorrelación rayos cósmicos–actividad solar a escala de ciclo solar</b> (11 años) cuando se disponga de series más largas.</li>'
 '</ul>'
 + note("Como trabajo a futuro, lo más inmediato es seguir midiendo con el MuNRA. Está calibrado, está en operación, y cada día que registra es datos que nos acercan a una muestra estadísticamente robusta. El siguiente paso grande es armar la red con los otros detectores MuNRA que se adquirieron, desplegarlos en distintos países, y comparar los decrecimientos entre estaciones y contra los datos de NMDB. Y para las correlaciones con campo magnético, aprendimos que hay que enfocarse en períodos de tormenta: en días calmos la señal es demasiado suave para que emerja el acoplamiento.")
 + '</section>',
])

# ---------- assemble ----------
def render(item):
    if isinstance(item, list):
        return "<section>\n" + "\n".join(item) + "\n</section>"
    return item
body = "\n".join(render(s) for s in slides)

tpl = open('deck_template.html').read()
# add team table style
tpl = tpl.replace('</style>',
  '.reveal table.team{ font-size:.46em; border-collapse:collapse; margin-top:1em; }'
  '.reveal table.team td{ padding:.22em .8em .22em 0; color:var(--ink); }'
  '.reveal table.team td:nth-child(2){ color:var(--muted); }'
  '.reveal table.team td:nth-child(3){ color:var(--accent); font-weight:700; }\n</style>')
open("Presentacion_Reto14.html","w",encoding="utf-8").write(tpl.replace("__BODY__", body))
print("ok deck4")
