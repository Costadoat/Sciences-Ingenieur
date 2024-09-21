set table "gnuplot/DS02/2.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-1:5] [] [] log10(10**t),-90+-180/3.1415957*atan(.01*10**t)+-180/3.1415957*atan(.0001*10**t)
