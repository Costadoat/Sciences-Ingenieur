set table "gnuplot/DS02/1.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-1:5] [] [] log10(10**t),20*log10(abs(1/(10**t)))+20*log10(abs(0.032/sqrt(1+(.01*10**t)**2)))+20*log10(abs(1/sqrt(1+(.0001*10**t)**2)))
