set table "gnuplot/DS03_prive/16.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:3] [] [] log10(10**t),-90+-180/3.1415957*atan(0.0016*10**t)+-180/3.1415957*atan(0.75*10**t)+--180/3.1415957*atan(0.1*10**t)
