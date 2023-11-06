import filters

ir = filters.Filter_infrared(filters.IRCUT_PIN)
vis = filters.Filter_visible(filters.SERVO_PIN)

ir.on()
vis.off()
