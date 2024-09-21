set table "gnuplot/DS02_prive/2.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:5] [] [] log10(10**t),20*log10(abs(1/(10**t)))+(t<log10(1/(.01))?20*log10(0.032):+20*log10(0.032/(.01))-20*log10(10**t))+(t<log10(1/(.0001))?20*log10(1):+20*log10(1/(.0001))-20*log10(10**t))
