set table "gnuplot/DS03_prive/10.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:3] [] [] log10(10**t),(t<log10(1/0.01)?20*log10(1):+20*log10(1*0.01)+20*log10(10**t))+(t<log10(1/(0.75))?20*log10(1):+20*log10(1/(0.75))-20*log10(10**t))
