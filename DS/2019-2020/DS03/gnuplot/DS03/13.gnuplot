set table "gnuplot/DS03/13.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:3] [] [] log10(10**t),20*log10(abs(10/(10**t)))+(t<log10(1/(0.0016))?20*log10(1):+20*log10(1/(0.0016))-20*log10(10**t))+(t<log10(1/(0.75))?20*log10(1):+20*log10(1/(0.75))-20*log10(10**t))+(t<log10(1/0.1)?20*log10(1):+20*log10(1*0.1)+20*log10(10**t))
