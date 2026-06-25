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
slides.append(
  '<section data-background-image="fondo.jpeg" data-background-size="cover" data-background-position="center" style="padding:0;width:1280px;height:720px;overflow:hidden;">'
  '<div style="position:absolute;inset:0;background:linear-gradient(100deg,rgba(0,0,0,0.55) 0%,rgba(0,0,0,0.25) 52%,transparent 72%);pointer-events:none;"></div>'
  '<div style="position:absolute;left:5%;bottom:14%;z-index:1;text-align:left;max-width:55%;">'
  '<h1 class="maintitle" style="font-weight:800;color:#fff;line-height:1.08;text-shadow:0 2px 12px rgba(0,0,0,.45);margin:0 0 0.4em 0;">'
  'RETO 14: Correlación Forbush<br>&amp; Pulsaciones<br>Geomagnéticas'
  '</h1>'
  '<div style="color:#fff;font-size:.55em;line-height:1.8;text-shadow:0 1px 6px rgba(0,0,0,.5);">'
  'Andre Jared Aguilar Ochoa · Universidad Nacional Autónoma de Honduras<br>'
  'Stephanie Carolina Cely Rodríguez · Universidad Nacional de Colombia<br>'
  'Peter Armando Perez Antaurco · Universidad Nacional de Ingeniería'
  '</div>'
  '</div>'
  '<div style="position:absolute;bottom:0;left:0;right:0;height:64px;background:#f2f4f7;border-top:2px solid #dde3ec;display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:2;">'
  '<img src="logo.jpeg" style="height:40px;object-fit:contain;" alt="EL-BONGÓ physics" />'
  '<div style="width:38px;height:38px;border-radius:50%;border:2.5px solid #1a4e8a;display:flex;align-items:center;justify-content:center;">'
  '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#1a4e8a" stroke-width="2" stroke-linecap="round">'
  '<circle cx="12" cy="12" r="10"/>'
  '<polygon points="12 2 14.5 9.5 12 8 9.5 9.5" fill="#1a4e8a" stroke="none"/>'
  '<polygon points="12 22 9.5 14.5 12 16 14.5 14.5" fill="#7a9ab5" stroke="none"/>'
  '</svg>'
  '</div>'
  '</div>'
  + note("Buenas. Somos el Equipo 1 y defendemos la parte de DÍAS DE TORMENTA del Reto 14: el decrecimiento Forbush y la respuesta geomagnética durante la tormenta del 19 al 21 de enero de 2026. Somos seis integrantes de Honduras, Colombia, Perú, El Salvador y Guatemala. Cada uno expondrá una parte y podrá responder sobre su aporte. [REPARTO sugerido: Aguilar—problema/enfoque; Tojil—física; Perez—MuNRA; Coloma—metodología; Cely—resultados MuNRA/EZIE; Jovel—resultados globales y conclusiones.]")
  + '</section>')

# ========== 1. FORMA DE ABORDAR EL PROBLEMA ==========
slides.append([
 divider("1 · FORMA DE ABORDAR EL PROBLEMA","Descripción del problema","","Objetivo, enfoque multi-instrumental e hipótesis de trabajo."),
 '<section><ul>'
 '<li class="fragment"><b>Objetivo:</b> caracterizar el <b>decrecimiento Forbush</b> y la respuesta geomagnética durante la <b>tormenta del 19–21 ene 2026</b>.</li>'
 '<li class="fragment"><b>Análisis multi-instrumental:</b> combinar análisis de rayos cósmicos (muones y neutrones), campo geomagnético y viento solar para ordenar la cadena causal del evento.</li>'
 '<li class="fragment"><b>Hipótesis:</b> la depresión de rayos cósmicos y la depresión del campo son respuestas acopladas a la CME.</li>'
 '</ul>'
 + note("El objetivo de nuestro equipo es caracterizar el decrecimiento Forbush y la respuesta geomagnética durante la tormenta del 19 al 21 de enero de 2026. La estrategia fue multi-instrumental: cruzar rayos cósmicos, campo magnético y viento solar para ordenar la secuencia causal. La hipótesis de trabajo es que la caída de rayos cósmicos y la depresión del campo son dos caras del mismo forzamiento: la CME.")
 + '</section>',
 '<section>'
 '<div class="grid2 fragment">'
 '<div class="card accentA"><h3>Etapa 1 — Sheath del ICME</h3><p>Plasma solar comprimido y turbulento entre el <b>choque interplanetario</b> y el material eyectado. Sus campos irregulares aumentan la dispersión en ángulo de ataque (pitch-angle scattering) de los rayos cósmicos → actúa como <b>barrera difusiva</b> → <b>caída inicial rápida</b>.</p></div>'
 '<div class="card accentA"><h3>Etapa 2 — Nube magnética</h3><p>El material eyectado porta una <b>cuerda de flujo</b> (campo fuerte y ordenado) que eleva el umbral de rigidez efectivo y suprime la difusión transversal de los rayos cósmicos → <b>depresión sostenida</b> durante el paso del ICME (12–48 h).</p></div>'
 '</div>'
 '<p class="fragment">Tres fases: <b>SSC</b> → <b>fase principal</b> (\\(B_z<0\\), corriente anular) → <b>recuperación</b>. Intensidad por \\(D_{st}\\): extrema \\(<-200\\) nT.</p>'
 '<p class="callout fragment"><b>CME</b> tormenta <b>Kp ≈ 8 (G4)</b> · \\(D_{st,\\text{mín}} = -236\\) nT.</p>'
 + note("La llamarada X1.95 del 18 de enero es radiación: llega en minutos y afecta la ionosfera, pero no deprime el campo geomagnético. Lo que causó la tormenta fue la CME asociada, el plasma magnetizado. El decrecimiento Forbush ocurre en dos etapas: primero el sheath del ICME —plasma turbulento entre el choque interplanetario y el material eyectado— actúa como barrera difusiva; después, la nube magnética con su cuerda de flujo suprime la difusión transversal y sostiene la depresión. La tormenta tiene tres fases: inicio súbito, fase principal con Bz al sur que forma la corriente anular, y recuperación. Nuestro evento alcanzó Kp cercano a 8, nivel G4, y un Dst mínimo de menos 236, categoría extrema.")
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
 '<section><h2>Observatorio de Rayos Cósmicos de México (MXCO)</h2>'
 '<div class="grid2">'
 '<div><ul class="tight">'
 '<li><b>Ubicación:</b> Ciudad Universitaria, UNAM, Ciudad de México — 19,33°N · 99,19°O</li>'
 '<li><b>Altitud:</b> 2 274 m s.n.m. · <b>Rigidez umbral:</b> 8,2 GV</li>'
 '<li><b>Detector 1:</b> Supermonitor de neutrones <b>6NM64</b> — 6 contadores proporcionales de BF₃ (componente nucleónica)</li>'
 '<li><b>Detector 2:</b> Telescopio de muones (componente dura)</li>'
 '<li><b>Rango de energía:</b> 8,5 – 200 GeV</li>'
 '</ul>'
 '<p class="callout" style="margin-top:.6em">MXCO es la estación NMDB más próxima a Honduras (≈ 570 km) y la de menor latitud del análisis → referencia regional clave para comparar con MuNRA.</p>'
 '</div>'
 '<div class="card accentA">'
 '<h3>¿Por qué importa la rigidez umbral?</h3>'
 '<p>La rigidez de corte (8,2 GV en MXCO vs. ≈ 1 GV en Calgary) determina qué partículas puede registrar cada estación. Estaciones con rigidez alta ven sólo rayos cósmicos de alta energía, que son menos modulados por la CME → los Forbush son más profundos en latitudes altas (<b>CALG −22,2 %</b>) que en latitudes bajas (<b>MXCO −16,7 %</b>).</p>'
 '</div>'
 '</div>'
 + note("Dedicamos un momento a MXCO porque es la estación NMDB más cercana a Honduras y la más comparable con MuNRA. Está en Ciudad Universitaria a 2274 metros sobre el nivel del mar, con una rigidez umbral de 8,2 gigavoltios. Tiene dos detectores: el supermonitor 6NM64 con seis contadores de trifluoruro de boro para la componente nucleónica, y un telescopio de muones para la componente dura. La rigidez umbral explica el gradiente latitudinal que vemos en los resultados: a mayor rigidez, mayor energía mínima detectable, menor modulación por la CME y por tanto Forbush menos profundo.")
 + '</section>',
 '<section><h2>Calibración del MuNRA</h2><div class="grid2">'
 '<div><ul class="tight">'
 '<li><b>Discretización</b> en intervalos de 60 s + corrección por <b>tiempo vivo</b> (tiempo muerto ≈ 10 %).</li>'
 '<li>Modelo ambiental \\(R=\\mu_R+\\beta\\,\\Delta P+\\alpha\\,\\Delta T\\); \\(\\alpha,\\beta\\) por <b>regresión múltiple</b> (Cramer) para romper la multicolinealidad P–T.</li>'
 '<li>Resultado base: <b>4,389 ± 0,295 cuentas s⁻¹</b>.</li></ul>'
 '<div class="card accentA" style="margin-top:.5em"><h3>Coeficientes</h3><p>\\(\\beta=-6{,}05\\times10^{-5}\\) (cuentas s⁻¹)/Pa<br>\\(\\alpha=-0{,}0487\\) (cuentas s⁻¹)/°C<br>Constantes, aplicados a la serie de tormenta.</p></div></div>'
 + img('munra_cont','MuNRA — línea base estable (1–12 ene): ≈ 4,5 cuentas s⁻¹.')
 + note("Sobre el MuNRA hicimos un pipeline de calibración propio. Primero, discretizamos los eventos en intervalos de 60 segundos y corregimos por tiempo vivo, porque el detector tiene un tiempo muerto cercano al 10 % que, de no corregirse, subestimaría el flujo. Segundo, modelamos los efectos ambientales: presión y temperatura. Como en Tegucigalpa presión y temperatura están muy correlacionadas, una covarianza simple da signos erróneos; por eso usamos regresión múltiple resuelta por la regla de Cramer para desacoplar los coeficientes. Obtuvimos una tasa base de 4,39 cuentas por segundo y coeficientes barométrico y térmico negativos, que aplicamos como constantes a la serie de la tormenta.")
 + '</section>',
 '<section><h2>Metodología de correlación</h2><ul>'
 '<li class="fragment"><b>Preprocesamiento EZIE-Mag:</b> filtro Hampel (mediana + MAD) — robusto a spikes electromagnéticos sin desplazar temporalmente los flancos de la tormenta, a diferencia de un promedio móvil.</li>'
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
 '<li><b>Vacío de 42,68 h</b>: la caída del campo (~13:00 UTC) coincide con la desconexión serial (~13:06 UTC). Atribuido a saturación del búfer por corrientes inducidas por la CME.</li>'
 '<li><b>Ceros intermitentes los días 22 y 23 de enero</b>: la tasa de conteo cae a cero en múltiples ocasiones — comportamiento que persiste tras el vacío principal y cuya causa aún debe determinarse.</li>'
 '</ul></div></div>'
 + note("Primer resultado, el MuNRA durante la tormenta. Se ve la caída del flujo de muones al iniciar el evento. Pero también un vacío de adquisición de casi 43 horas: la caída del campo magnético a las 13:00 coincide al minuto con la desconexión del detector a las 13:06. Lo atribuimos a una saturación del búfer por las corrientes que induce la CME. Es una limitación que reconocemos: con el MuNRA no pudimos cubrir el mínimo del Forbush, y por eso nos apoyamos en los neutrones.")
 + '</section>',
 '<section><h2>Acoplamiento EZIE-Mag ↔ MuNRA</h2><div class="grid2">'
 + img('corr_ezie_munra','Correlación móvil tasa de muones vs campo horizontal.')
 + img('scatter','COE vs EZIE-Mag: r = 0,968 (estaciones a ≈ 620 km).') + '</div>'
 '<p class="callout">Con ventanas de 12–24 h emerge \\(r>0{,}6\\) en la fase de recuperación: la recuperación del campo y la del flujo son la misma respuesta física.</p>'
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
 '<section><h2>Decrecimiento Forbush en NMDB México (MXCO)</h2>'
 '<div class="grid2" style="align-items:start">'
 + img('forbush','Fig. 17 — NMDB MXCO (% vs ref.) y B_total EZIE-Mag MAGHO-1.')
 + '<div><ul class="tight">'
 '<li><b>FD_mín = −16,7 %</b> en MXCO (rigidez 8,2 GV).</li>'
 '<li><b>Dst_mín = −236 nT</b> (tormenta extrema G4).</li>'
 '<li><b>SSC</b> ~19 ene 00:00 UTC → fase principal en ≈ 10 h.</li>'
 '<li><b>B_total</b> EZIE-Mag: compresión inicial antes del mínimo del campo.</li>'
 '<li class="callout" style="list-style:none;margin-top:.5em">El Forbush precede al Dst: la barrera magnética de la CME modula los rayos cósmicos antes de comprimir la magnetosfera interna.</li>'
 '</ul></div></div>'
 + note("Esta es la figura 17 del informe. Muestra en el panel superior la variación porcentual del flujo de neutrones en MXCO (NMDB México, rigidez umbral 8,2 GV) junto con B_total de EZIE-Mag a 1 minuto y 1 hora. En el panel central el Dst de Kyoto. En el panel inferior la correlación cruzada con retardo: el máximo en tau negativo indica que el decrecimiento Forbush precede al mínimo del Dst, consistente con la geometría de la CME que primero modula los rayos cósmicos antes de comprimir la magnetosfera.")
 + '</section>',
 '<section><h2>Correlaciones y retardos temporales</h2><div class="grid2">'
 + img('pearson','Fig. 22 — Matriz de correlación de Pearson entre NMDB, campo y parámetros heliosféricos.')
 + img('lags','Fig. 23 — Correlación cruzada de NMDBprom con parámetros heliosféricos en función del retardo.')
 + '</div>'
 '<div class="grid2 fragment" style="margin-top:.3em;font-size:.82em">'
 '<table class="mini"><tr><th></th><th>MXCO</th><th>NEWK</th><th>CALG</th></tr>'
 '<tr><td>Latitud</td><td>19,3°N</td><td>40,0°N</td><td>51,1°N</td></tr>'
 '<tr><td>Caída FD</td><td>−16,7 %</td><td>−20,4 %</td><td>−22,2 %</td></tr></table>'
 '<ul class="tight" style="font-size:.9em"><li>Factores dominantes: \\(V_{sw}\\) (<b>r=−0,86</b>), \\(D_{st}\\) (<b>0,83</b>), \\(B_{total}\\) (<b>−0,76</b>).</li>'
 '<li>\\(\\text{IMF}\\,B_z\\) débil (<b>r=−0,27</b>): dispara reconexión, no fija profundidad.</li>'
 '<li>\\(\\tau^*=-3\\) h \\(V_{sw}\\); \\(\\approx0\\) h \\(B_{total}\\)/\\(D_{st}\\); \\(\\tau^*=-7\\) h \\(B_z\\) (anticipa).</li></ul>'
 '</div>'
 + note("La matriz y los retardos. Las tres NMDB se mueven juntas con r mayor a 0,97: el evento fue global y coherente. Velocidad del viento solar y Dst son los factores dominantes del Forbush; el campo interplanetario total también contribuye. La Bz es débil como predictor de profundidad porque su papel es disparar la reconexión, no fijar la amplitud. Y el gradiente latitudinal en la tabla confirma la dependencia de rigidez geomagnética: a mayor latitud, menor blindaje, mayor supresión. El τ* de menos 7 horas de Bz es el único parámetro que anticipa el evento: cuando la componente se vuelve al sur, la magnetosfera ya está abierta antes de que llegue el plasma.")
 + '</section>',
])

# ========== 4. QUÉ ENTREGAMOS ==========
slides.append([
 divider("4 · ¿QUÉ ENTREGAMOS?","Entregables del equipo","",
   "Breve: qué productos entregamos."),
 '<section><h2>Entregables</h2><ul>'
 '<li class="fragment"><b>Informe </b> del evento de tormenta.</li>'
 '<li class="fragment"><b>Pipeline de calibración del MuNRA</b> en Python: tiempo vivo, corrección barométrica/térmica y serie en cuentas s⁻¹.</li>'
 '<li class="fragment"><b>Series sincronizadas y análisis de correlación</b> (Fisher, cruzada con retardo, móvil) entre MuNRA, EZIE-Mag, NMDB y OMNIWeb.</li>'
 '<li class="fragment"> caracterización del MuNRA, acoplamiento campo–muones, evolución de la tormenta y matriz de correlaciones.</li></ul>'
 + note("¿Qué entregamos? Un informe científico del evento de tormenta, ya con las correcciones de física. Un pipeline de calibración del MuNRA en Python, que convierte los eventos crudos en una serie corregida en cuentas por segundo. Las series sincronizadas y todo el análisis de correlación entre los cuatro instrumentos. Y el conjunto de figuras y tablas que sustentan los resultados.")
 + '</section>',
])

# ========== 5. CONCLUSIONES ==========
slides.append([
 divider("5 · CONCLUSIONES","Conclusiones","","Limitaciones del MuNRA, verificación con NMDB, correlaciones geomagnéticas, retardos temporales y trabajo a futuro."),

 # --- 5a. MuNRA: logros y limitaciones ---
 '<section><h2>Limitaciones del MuNRA</h2><div class="grid2"><div><ul class="tight">'
 '<li class="fragment"><b>Tasa basal estable:</b> 4,39 ± 0,29 cuentas s⁻¹ — detector calibrado y en operación.</li>'
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
 '<li class="fragment"><b>EZIE-Mag ↔ MuNRA</b> (ventanas 12–24 h): \\(r>0{,}6\\) en la recuperación (valor exacto e IC reportados en §4.8.3 del informe) → campo y flujo de rayos cósmicos son respuestas acopladas a la misma CME.</li>'
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
 '<li class="fragment"><b>\\(\\tau^*=-3\\) h en \\(V_{sw}\\to\\) NMDB</b>: el viento solar en L1 <em>anticipa</em> la caída de rayos cósmicos — reflejo del tiempo de tránsito L1→Tierra más la formación de la barrera magnética (confirmado en §3.3.6 del informe, \\(r_{máx}=-0{,}840\\)).</li>'
 '<li class="fragment"><b>\\(\\tau^*\\approx0\\) h en \\(D_{st}\\)</b>: la depresión geomagnética y el Forbush son prácticamente <em>simultáneas</em> a resolución horaria — ambas son respuestas directas al mismo forzamiento de la CME.</li>'
 '<li class="fragment"><b>Lag = −7 h en \\(\\text{IMF}\\,B_z\\)</b>: \\(B_z\\) es la única variable que <em>anticipa</em> el evento — gatillo de la reconexión magnética que abre la magnetosfera antes del plasma de la CME.</li>'
 '<li class="fragment"><b>Lag ≈ 1–3 h en \\(B_{total}\\) y densidad</b>: estructura secuencial interna de la CME — primero la magnetosheath turbulenta (campo elevado), luego la nube magnética densa.</li>'
 '<li class="fragment">En conjunto, los retardos trazan la <b>cadena causal</b>: \\(B_z \\to\\) reconexión \\(\\to\\) tormenta + barrera para rayos cósmicos.</li>'
 '<li class="fragment"><em>Limitación:</em> análisis a <b>resolución horaria</b> → puede enmascarar retardos más finos (subhorarios) relevantes durante la fase de inicio de la tormenta.</li>'
 '</ul>'
 + note("Este es uno de los resultados más ricos del análisis. El viento solar en L1 anticipa la caída del NMDB en 3 horas: ese retardo refleja el tiempo de tránsito desde el punto L1 hasta la magnetosfera terrestre más el tiempo que tarda en formarse la barrera magnética. Por eso tau es menos 3, no cero — es una cadena física, no una coincidencia. El Dst, en cambio, sí es simultáneo al Forbush a resolución horaria: ambos son respuestas directas a la misma CME, solo con mecanismos distintos. El IMF Bz anticipa el evento en 7 horas porque es el parámetro que controla la reconexión: cuando Bz se vuelve al sur la magnetosfera se abre, y eso prepara el camino antes de que llegue el plasma. Los retardos en Btotal y densidad reflejan la estructura interna de la CME: primero el sheath del ICME (plasma turbulento entre choque y material eyectado), luego la nube magnética.")
 + '</section>',

 # --- 5d. Red geomagnética regional ---
 '<section><h2>Red geomagnética regional</h2><ul class="tight">'
 '<li class="fragment"><b>COE (México, 19,8°N) ↔ EZIE-Mag (Honduras, 14,1°N)</b>: \\(r = 0{,}968\\), lag \\(\\tau^*=0\\) h — coherencia a gran escala pese a 620 km de separación.</li>'
 '<li class="fragment">Desde 2026 Honduras tiene registro continuo del magnetómetro; muestra <b>mejor correlación con México que con Puerto Rico</b>.</li>'
 '<li class="fragment">Puerto Rico es una isla más influenciada por los campos magnéticos del océano y su posición geográfica introduce un comportamiento diferente.</li>'
 '<li class="fragment">El <b>campo magnético terrestre no es simétrico ni uniforme</b>: México y Honduras comparten un patrón regional similar, lo que valida usar COE como referencia continental para EZIE-Mag.</li>'
 '</ul>'
 + note("La alta correlación entre los dos magnetómetros, México y Honduras, es un resultado importante en sí mismo. Nos dice que la perturbación geomagnética fue coherente a escala regional, no local. Y el hecho de que Honduras correlacione mejor con México que con Puerto Rico tiene una explicación física: el campo magnético terrestre no es uniforme. Puerto Rico, al ser una isla, está más influenciada por los campos magnéticos del océano, que actúan como un conductor que distorsiona la señal. México y Honduras, siendo continentales y cercanos en longitud, comparten un patrón de campo regional más similar.")
 + '</section>',

 # --- 5e. Trabajo a futuro ---
 '<section data-background-gradient="linear-gradient(135deg,#0b1f3a,#123a63)">'
 '<div class="dlabel" style="font-size:.9em">TRABAJO A FUTURO</div>'
 '<ul style="margin-top:1.2em;font-size:.78em;line-height:1.7">'
 '<li class="fragment">Ampliar el <b>registro temporal del MuNRA</b> (ya calibrado y en operación) para obtener muestras estadísticamente significativas del Forbush.</li>'
 '<li class="fragment"><b>Determinar por qué el conteo de muones cae a cero</b> con frecuencia (ocurrió durante la tormenta y también los días 22 y 23 de enero) — diagnóstico del búfer del detector.</li>'
 '<li class="fragment">Desplegar los <b>otros detectores MuNRA adquiridos en distintos países</b> → construir una red multi-punto y comparar decrecimientos entre sí.</li>'
 '<li class="fragment">Comparar la <b>red MuNRA con datos NMDB</b> para validar que los muones capturan los mismos decrecimientos que los neutrones.</li>'
 '<li class="fragment">Para correlaciones con <b>campo magnético</b>: enfocarse en períodos de tormenta — en días calmos la correlación es débil; el acoplamiento solo es significativo durante eventos extremos.</li>'
 '<li class="fragment">Estudiar la <b>anticorrelación rayos cósmicos–actividad solar a escala de ciclo solar</b> (11 años) cuando se disponga de series más largas.</li>'
 '</ul>'
 + note("Como trabajo a futuro, lo más inmediato es seguir midiendo con el MuNRA. Está calibrado, está en operación, y cada día que registra es datos que nos acercan a una muestra estadísticamente robusta. El siguiente paso grande es armar la red con los otros detectores MuNRA que se adquirieron, desplegarlos en distintos países, y comparar los decrecimientos entre estaciones y contra los datos de NMDB. Y para las correlaciones con campo magnético, aprendimos que hay que enfocarse en períodos de tormenta: en días calmos la señal es demasiado suave para que emerja el acoplamiento.")
 + '</section>',
])

# ========== 6. REFERENCIAS ==========
slides.append(
  '<section data-background-gradient="linear-gradient(135deg,#0b1f3a,#123a63)">'
  '<h2 style="color:#fff;font-size:.9em;margin-bottom:.6em;letter-spacing:.05em;text-transform:uppercase;">Referencias principales</h2>'
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:.45em 1.2em;font-size:.42em;line-height:1.55;color:#d4e0f0;text-align:left;">'
  '<div><b style="color:#7eb8f7;">[1]</b> Cane, H. V. (2000). Coronal mass ejections and Forbush decreases. <em>Space Science Reviews</em>, 93(1–2):55–77.</div>'
  '<div><b style="color:#7eb8f7;">[2]</b> Belov, A. (2008). Forbush effects and their connection with solar, interplanetary and geomagnetic phenomena. <em>Proc. IAU</em>, 4(S257):439–450.</div>'
  '<div><b style="color:#7eb8f7;">[3]</b> Lockwood, J. A. (1971). Forbush decreases in the cosmic radiation. <em>Space Science Reviews</em>, 12(5):658–715.</div>'
  '<div><b style="color:#7eb8f7;">[4]</b> Gonzalez, W. D. et al. (1994). What is a geomagnetic storm? <em>J. Geophys. Res.</em>, 99(A4):5771–5792.</div>'
  '<div><b style="color:#7eb8f7;">[5]</b> Campbell, W. H. (2003). <em>Introduction to Geomagnetic Fields</em>. Cambridge University Press, 2nd ed.</div>'
  '<div><b style="color:#7eb8f7;">[6]</b> Hampel, F. R. (1974). The influence curve and its role in robust estimation. <em>J. Amer. Stat. Assoc.</em>, 69(346):383–393.</div>'
  '<div><b style="color:#7eb8f7;">[7]</b> Sargsyan, B. &amp; Chilingarian, A. (2026). Continued activity of cycle 25: largest in 20 years — GLE and Forbush decrease. <em>arXiv</em>:2601.19289.</div>'
  '<div><b style="color:#7eb8f7;">[8]</b> Pandey, P. (2026). Forbush depression at Oulu in January 2026. <em>Int. J. Science and Research</em>, 15(2).</div>'
  '<div><b style="color:#7eb8f7;">[9]</b> Yee, J.-H. et al. (2026). Status and latest results from NASA EZIE. <em>EGU General Assembly 2026</em>, EGU26-8389.</div>'
  '<div><b style="color:#7eb8f7;">[10]</b> Pahud, D. M. et al. (2009). Ground-based Pc5 ULF wave power: solar wind speed and MLT dependence. <em>J. Atm. Sol.-Terr. Phys.</em>, 71(10–11):1082–1092.</div>'
  '</div>'
  + note("Estas son las referencias más relevantes. El núcleo físico del decrecimiento Forbush descansa en Cane 2000, Belov 2008 y Lockwood 1971. La definición de tormenta geomagnética en Gonzalez 1994. El sistema Sq en Campbell 2003. El filtro Hampel para el preprocesamiento en Hampel 1974. Y los dos artículos de 2026 de Sargsyan y Pandey que documentan exactamente el mismo evento de enero que analizamos.")
  + '</section>'
)

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
open("index.html","w",encoding="utf-8").write(tpl.replace("__BODY__", body))
print("ok deck4")
