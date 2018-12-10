

# https://www.amazon.com/dp/B077X95LRZ/ref=psdc_2314207011_t2_B016O47134?th=1
# https://www.menards.com/main/tools-hardware/sheet-metal-rods/hillman-reg-aluminum-round-tubes/11395/p-1444432418537.htm

#setwd("C:/dev/LEDclock")

pdf("rpi_clock.pdf")

lim = .5
plot(0,type="n",main="",xlab="",ylab="",ylim=c(-lim,lim),xlim=c(-lim,lim),col="white",yaxt="n",xaxt="n")
# axis(2, axTicks(2), format(axTicks(2), scientific = F,big.mark=',')) 

abline(h=0,col="gray")
abline(v=0,col="gray")

thickness = .5/12 # half inch

theta = seq(0,2*pi,length.out = 1000)

tube = function(c){
  r = c/pi/2
  for(i in seq(r-thickness,r,length.out=100)) lines(i*cos(theta),i*sin(theta),col = "blue")
  lines(r*cos(theta),r*sin(theta),lwd=2)
  lines((r-thickness)*cos(theta),(r-thickness)*sin(theta),lwd=2)
  return(r)
}

lines(.5*cos(theta),.5*sin(theta),lwd=3) # outer edge of the base board
tube(2.5)
tube(2)
tube(1.5)
tube(1)

2.5+2+1.5+1
dev.off()
