	.cpu cortex-m4
	.eabi_attribute 27, 1
	.eabi_attribute 28, 1
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 1
	.eabi_attribute 30, 6
	.eabi_attribute 34, 1
	.eabi_attribute 18, 4
	.file	"spis.c"
	.text
.Ltext0:
	.section	.text.sd_mbr_command,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_mbr_command, %function
sd_mbr_command:
.LFB138:
	.file 1 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf52/nrf_mbr.h"
	.loc 1 257 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 1 257 1
	.syntax unified
@ 257 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf52/nrf_mbr.h" 1
	svc #24
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE138:
	.size	sd_mbr_command, .-sd_mbr_command
	.section	.text.sd_mutex_new,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_mutex_new, %function
sd_mutex_new:
.LFB164:
	.file 2 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h"
	.loc 2 452 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 452 1
	.syntax unified
@ 452 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #44
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE164:
	.size	sd_mutex_new, .-sd_mutex_new
	.section	.text.sd_mutex_acquire,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_mutex_acquire, %function
sd_mutex_acquire:
.LFB165:
	.loc 2 461 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 461 1
	.syntax unified
@ 461 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #45
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE165:
	.size	sd_mutex_acquire, .-sd_mutex_acquire
	.section	.text.sd_mutex_release,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_mutex_release, %function
sd_mutex_release:
.LFB166:
	.loc 2 469 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 469 1
	.syntax unified
@ 469 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #46
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE166:
	.size	sd_mutex_release, .-sd_mutex_release
	.section	.text.sd_rand_application_pool_capacity_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_rand_application_pool_capacity_get, %function
sd_rand_application_pool_capacity_get:
.LFB167:
	.loc 2 477 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 477 1
	.syntax unified
@ 477 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #47
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE167:
	.size	sd_rand_application_pool_capacity_get, .-sd_rand_application_pool_capacity_get
	.section	.text.sd_rand_application_bytes_available_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_rand_application_bytes_available_get, %function
sd_rand_application_bytes_available_get:
.LFB168:
	.loc 2 485 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 485 1
	.syntax unified
@ 485 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #48
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE168:
	.size	sd_rand_application_bytes_available_get, .-sd_rand_application_bytes_available_get
	.section	.text.sd_rand_application_vector_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_rand_application_vector_get, %function
sd_rand_application_vector_get:
.LFB169:
	.loc 2 495 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 495 1
	.syntax unified
@ 495 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #49
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE169:
	.size	sd_rand_application_vector_get, .-sd_rand_application_vector_get
	.section	.text.sd_power_reset_reason_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_reset_reason_get, %function
sd_power_reset_reason_get:
.LFB170:
	.loc 2 503 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 503 1
	.syntax unified
@ 503 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #52
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE170:
	.size	sd_power_reset_reason_get, .-sd_power_reset_reason_get
	.section	.text.sd_power_reset_reason_clr,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_reset_reason_clr, %function
sd_power_reset_reason_clr:
.LFB171:
	.loc 2 511 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 511 1
	.syntax unified
@ 511 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #53
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE171:
	.size	sd_power_reset_reason_clr, .-sd_power_reset_reason_clr
	.section	.text.sd_power_mode_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_mode_set, %function
sd_power_mode_set:
.LFB172:
	.loc 2 520 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 520 1
	.syntax unified
@ 520 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #50
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE172:
	.size	sd_power_mode_set, .-sd_power_mode_set
	.section	.text.sd_power_system_off,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_system_off, %function
sd_power_system_off:
.LFB173:
	.loc 2 526 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 526 1
	.syntax unified
@ 526 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #51
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE173:
	.size	sd_power_system_off, .-sd_power_system_off
	.section	.text.sd_power_pof_enable,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_pof_enable, %function
sd_power_pof_enable:
.LFB174:
	.loc 2 537 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 537 1
	.syntax unified
@ 537 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #54
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE174:
	.size	sd_power_pof_enable, .-sd_power_pof_enable
	.section	.text.sd_power_usbpwrrdy_enable,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_usbpwrrdy_enable, %function
sd_power_usbpwrrdy_enable:
.LFB175:
	.loc 2 550 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 550 1
	.syntax unified
@ 550 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #77
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE175:
	.size	sd_power_usbpwrrdy_enable, .-sd_power_usbpwrrdy_enable
	.section	.text.sd_power_usbdetected_enable,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_usbdetected_enable, %function
sd_power_usbdetected_enable:
.LFB176:
	.loc 2 563 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 563 1
	.syntax unified
@ 563 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #78
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE176:
	.size	sd_power_usbdetected_enable, .-sd_power_usbdetected_enable
	.section	.text.sd_power_usbremoved_enable,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_usbremoved_enable, %function
sd_power_usbremoved_enable:
.LFB177:
	.loc 2 576 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 576 1
	.syntax unified
@ 576 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #79
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE177:
	.size	sd_power_usbremoved_enable, .-sd_power_usbremoved_enable
	.section	.text.sd_power_usbregstatus_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_usbregstatus_get, %function
sd_power_usbregstatus_get:
.LFB178:
	.loc 2 586 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 586 1
	.syntax unified
@ 586 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #80
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE178:
	.size	sd_power_usbregstatus_get, .-sd_power_usbregstatus_get
	.section	.text.sd_power_pof_threshold_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_pof_threshold_set, %function
sd_power_pof_threshold_set:
.LFB179:
	.loc 2 599 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 599 1
	.syntax unified
@ 599 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #55
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE179:
	.size	sd_power_pof_threshold_set, .-sd_power_pof_threshold_set
	.section	.text.sd_power_pof_thresholdvddh_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_pof_thresholdvddh_set, %function
sd_power_pof_thresholdvddh_set:
.LFB180:
	.loc 2 612 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 612 1
	.syntax unified
@ 612 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #56
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE180:
	.size	sd_power_pof_thresholdvddh_set, .-sd_power_pof_thresholdvddh_set
	.section	.text.sd_power_ram_power_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_ram_power_set, %function
sd_power_ram_power_set:
.LFB181:
	.loc 2 621 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 621 1
	.syntax unified
@ 621 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #57
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE181:
	.size	sd_power_ram_power_set, .-sd_power_ram_power_set
	.section	.text.sd_power_ram_power_clr,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_ram_power_clr, %function
sd_power_ram_power_clr:
.LFB182:
	.loc 2 630 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 630 1
	.syntax unified
@ 630 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #58
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE182:
	.size	sd_power_ram_power_clr, .-sd_power_ram_power_clr
	.section	.text.sd_power_ram_power_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_ram_power_get, %function
sd_power_ram_power_get:
.LFB183:
	.loc 2 639 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 639 1
	.syntax unified
@ 639 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #59
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE183:
	.size	sd_power_ram_power_get, .-sd_power_ram_power_get
	.section	.text.sd_power_gpregret_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_gpregret_set, %function
sd_power_gpregret_set:
.LFB184:
	.loc 2 648 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 648 1
	.syntax unified
@ 648 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #60
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE184:
	.size	sd_power_gpregret_set, .-sd_power_gpregret_set
	.section	.text.sd_power_gpregret_clr,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_gpregret_clr, %function
sd_power_gpregret_clr:
.LFB185:
	.loc 2 657 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 657 1
	.syntax unified
@ 657 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #61
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE185:
	.size	sd_power_gpregret_clr, .-sd_power_gpregret_clr
	.section	.text.sd_power_gpregret_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_gpregret_get, %function
sd_power_gpregret_get:
.LFB186:
	.loc 2 666 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 666 1
	.syntax unified
@ 666 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #62
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE186:
	.size	sd_power_gpregret_get, .-sd_power_gpregret_get
	.section	.text.sd_power_dcdc_mode_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_dcdc_mode_set, %function
sd_power_dcdc_mode_set:
.LFB187:
	.loc 2 675 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 675 1
	.syntax unified
@ 675 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #63
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE187:
	.size	sd_power_dcdc_mode_set, .-sd_power_dcdc_mode_set
	.section	.text.sd_power_dcdc0_mode_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_power_dcdc0_mode_set, %function
sd_power_dcdc0_mode_set:
.LFB188:
	.loc 2 686 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 686 1
	.syntax unified
@ 686 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #64
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE188:
	.size	sd_power_dcdc0_mode_set, .-sd_power_dcdc0_mode_set
	.section	.text.sd_clock_hfclk_request,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_clock_hfclk_request, %function
sd_clock_hfclk_request:
.LFB189:
	.loc 2 698 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 698 1
	.syntax unified
@ 698 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #66
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE189:
	.size	sd_clock_hfclk_request, .-sd_clock_hfclk_request
	.section	.text.sd_clock_hfclk_release,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_clock_hfclk_release, %function
sd_clock_hfclk_release:
.LFB190:
	.loc 2 709 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 709 1
	.syntax unified
@ 709 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #67
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE190:
	.size	sd_clock_hfclk_release, .-sd_clock_hfclk_release
	.section	.text.sd_clock_hfclk_is_running,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_clock_hfclk_is_running, %function
sd_clock_hfclk_is_running:
.LFB191:
	.loc 2 720 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 720 1
	.syntax unified
@ 720 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #68
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE191:
	.size	sd_clock_hfclk_is_running, .-sd_clock_hfclk_is_running
	.section	.text.sd_app_evt_wait,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_app_evt_wait, %function
sd_app_evt_wait:
.LFB192:
	.loc 2 748 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 748 1
	.syntax unified
@ 748 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #65
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE192:
	.size	sd_app_evt_wait, .-sd_app_evt_wait
	.section	.text.sd_ppi_channel_enable_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_channel_enable_get, %function
sd_ppi_channel_enable_get:
.LFB193:
	.loc 2 756 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 756 1
	.syntax unified
@ 756 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #32
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE193:
	.size	sd_ppi_channel_enable_get, .-sd_ppi_channel_enable_get
	.section	.text.sd_ppi_channel_enable_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_channel_enable_set, %function
sd_ppi_channel_enable_set:
.LFB194:
	.loc 2 764 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 764 1
	.syntax unified
@ 764 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #33
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE194:
	.size	sd_ppi_channel_enable_set, .-sd_ppi_channel_enable_set
	.section	.text.sd_ppi_channel_enable_clr,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_channel_enable_clr, %function
sd_ppi_channel_enable_clr:
.LFB195:
	.loc 2 772 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 772 1
	.syntax unified
@ 772 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #34
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE195:
	.size	sd_ppi_channel_enable_clr, .-sd_ppi_channel_enable_clr
	.section	.text.sd_ppi_channel_assign,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_channel_assign, %function
sd_ppi_channel_assign:
.LFB196:
	.loc 2 783 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 783 1
	.syntax unified
@ 783 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #35
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE196:
	.size	sd_ppi_channel_assign, .-sd_ppi_channel_assign
	.section	.text.sd_ppi_group_task_enable,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_group_task_enable, %function
sd_ppi_group_task_enable:
.LFB197:
	.loc 2 792 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 792 1
	.syntax unified
@ 792 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #36
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE197:
	.size	sd_ppi_group_task_enable, .-sd_ppi_group_task_enable
	.section	.text.sd_ppi_group_task_disable,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_group_task_disable, %function
sd_ppi_group_task_disable:
.LFB198:
	.loc 2 801 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 801 1
	.syntax unified
@ 801 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #37
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE198:
	.size	sd_ppi_group_task_disable, .-sd_ppi_group_task_disable
	.section	.text.sd_ppi_group_assign,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_group_assign, %function
sd_ppi_group_assign:
.LFB199:
	.loc 2 811 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 811 1
	.syntax unified
@ 811 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #38
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE199:
	.size	sd_ppi_group_assign, .-sd_ppi_group_assign
	.section	.text.sd_ppi_group_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ppi_group_get, %function
sd_ppi_group_get:
.LFB200:
	.loc 2 821 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 821 1
	.syntax unified
@ 821 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #39
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE200:
	.size	sd_ppi_group_get, .-sd_ppi_group_get
	.section	.text.sd_radio_notification_cfg_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_radio_notification_cfg_set, %function
sd_radio_notification_cfg_set:
.LFB201:
	.loc 2 852 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 852 1
	.syntax unified
@ 852 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #69
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE201:
	.size	sd_radio_notification_cfg_set, .-sd_radio_notification_cfg_set
	.section	.text.sd_ecb_block_encrypt,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ecb_block_encrypt, %function
sd_ecb_block_encrypt:
.LFB202:
	.loc 2 868 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 868 1
	.syntax unified
@ 868 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #70
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE202:
	.size	sd_ecb_block_encrypt, .-sd_ecb_block_encrypt
	.section	.text.sd_ecb_blocks_encrypt,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ecb_blocks_encrypt, %function
sd_ecb_blocks_encrypt:
.LFB203:
	.loc 2 885 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 885 1
	.syntax unified
@ 885 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #71
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE203:
	.size	sd_ecb_blocks_encrypt, .-sd_ecb_blocks_encrypt
	.section	.text.sd_evt_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_evt_get, %function
sd_evt_get:
.LFB204:
	.loc 2 896 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 896 1
	.syntax unified
@ 896 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #75
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE204:
	.size	sd_evt_get, .-sd_evt_get
	.section	.text.sd_temp_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_temp_get, %function
sd_temp_get:
.LFB205:
	.loc 2 907 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 907 1
	.syntax unified
@ 907 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #76
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE205:
	.size	sd_temp_get, .-sd_temp_get
	.section	.text.sd_flash_write,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_flash_write, %function
sd_flash_write:
.LFB206:
	.loc 2 944 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 944 1
	.syntax unified
@ 944 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #41
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE206:
	.size	sd_flash_write, .-sd_flash_write
	.section	.text.sd_flash_page_erase,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_flash_page_erase, %function
sd_flash_page_erase:
.LFB207:
	.loc 2 976 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 976 1
	.syntax unified
@ 976 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #40
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE207:
	.size	sd_flash_page_erase, .-sd_flash_page_erase
	.section	.text.sd_radio_session_open,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_radio_session_open, %function
sd_radio_session_open:
.LFB208:
	.loc 2 1000 2
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 1000 2
	.syntax unified
@ 1000 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #72
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE208:
	.size	sd_radio_session_open, .-sd_radio_session_open
	.section	.text.sd_radio_session_close,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_radio_session_close, %function
sd_radio_session_close:
.LFB209:
	.loc 2 1013 2
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 1013 2
	.syntax unified
@ 1013 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #73
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE209:
	.size	sd_radio_session_close, .-sd_radio_session_close
	.section	.text.sd_radio_request,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_radio_request, %function
sd_radio_request:
.LFB210:
	.loc 2 1050 2
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 1050 2
	.syntax unified
@ 1050 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #74
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE210:
	.size	sd_radio_request, .-sd_radio_request
	.section	.text.sd_protected_register_write,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_protected_register_write, %function
sd_protected_register_write:
.LFB211:
	.loc 2 1071 1
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 2 1071 1
	.syntax unified
@ 1071 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #43
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	nop
	mov	r0, r3
.LFE211:
	.size	sd_protected_register_write, .-sd_protected_register_write
	.section	.text.log_timestamp_get,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	log_timestamp_get, %function
log_timestamp_get:
.LFB286:
	.file 3 "../../mesh/core/include/log.h"
	.loc 3 199 1
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	.loc 3 209 20
	ldr	r3, .L52
	ldr	r3, [r3, #1284]
	.loc 3 211 1
	mov	r0, r3
	bx	lr
.L53:
	.align	2
.L52:
	.word	1073811456
.LFE286:
	.size	log_timestamp_get, .-log_timestamp_get
	.global	SWITCH2SPI
	.section	.bss.SWITCH2SPI,"aw",%nobits
	.type	SWITCH2SPI, %object
	.size	SWITCH2SPI, 1
SWITCH2SPI:
	.space	1
	.section	.rodata.spis,"a"
	.align	2
	.type	spis, %object
	.size	spis, 8
spis:
	.word	1073758208
	.byte	1
	.space	3
	.section	.rodata.m_rx_length,"a"
	.align	2
	.type	m_rx_length, %object
	.size	m_rx_length, 4
m_rx_length:
	.word	100
	.section	.rodata.m_tx_max__length,"a"
	.align	2
	.type	m_tx_max__length, %object
	.size	m_tx_max__length, 4
m_tx_max__length:
	.word	100
	.section	.bss.m_tx_length,"aw",%nobits
	.align	2
	.type	m_tx_length, %object
	.size	m_tx_length, 4
m_tx_length:
	.space	4
	.section	.bss.m_tx_buf,"aw",%nobits
	.align	2
	.type	m_tx_buf, %object
	.size	m_tx_buf, 4
m_tx_buf:
	.space	4
	.section	.bss.m_rx_buf,"aw",%nobits
	.align	2
	.type	m_rx_buf, %object
	.size	m_rx_buf, 4
m_rx_buf:
	.space	4
	.section	.bss.spis_xfer_done,"aw",%nobits
	.type	spis_xfer_done, %object
	.size	spis_xfer_done, 1
spis_xfer_done:
	.space	1
	.section .rodata
	.align	2
.LC1:
	.ascii	"/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0."
	.ascii	"0_src/examples/beaconing/src/spis.c\000"
	.align	2
.LC2:
	.ascii	"Transfer completed. Received: %s, first:%d \012\000"
	.section	.text.spis_event_handler,"ax",%progbits
	.align	1
	.global	spis_event_handler
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	spis_event_handler, %function
spis_event_handler:
.LFB287:
	.file 4 "/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0.0_src/examples/beaconing/src/spis.c"
	.loc 4 36 1
	@ args = 0, pretend = 0, frame = 24
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
.LCFI0:
	sub	sp, sp, #40
.LCFI1:
	add	r3, sp, #20
	stm	r3, {r0, r1, r2}
	.loc 4 37 14
	ldrb	r3, [sp, #20]	@ zero_extendqisi2
	.loc 4 37 8
	cmp	r3, #1
	bne	.L57
.LBB2:
	.loc 4 39 24
	ldr	r3, .L58
	movs	r2, #1
	strb	r2, [r3]
	.loc 4 40 9
	ldr	r3, .L58+4
	ldr	r3, [r3]
	and	r3, r3, #16384
	cmp	r3, #0
	beq	.L56
	.loc 4 40 9 is_stmt 0 discriminator 1
	ldr	r3, .L58+8
	ldr	r3, [r3]
	cmp	r3, #3
	ble	.L56
	.loc 4 40 9 discriminator 2
	ldr	r4, .L58+12
	bl	log_timestamp_get
	mov	r1, r0
	ldr	r3, .L58+16
	ldr	r3, [r3]
	ldr	r2, .L58+16
	ldr	r2, [r2]
	ldrb	r2, [r2]	@ zero_extendqisi2
	str	r2, [sp, #8]
	str	r3, [sp, #4]
	ldr	r3, .L58+20
	str	r3, [sp]
	mov	r3, r1
	movs	r2, #40
	mov	r1, r4
	movs	r0, #4
	bl	log_printf
.L56:
	.loc 4 42 17 is_stmt 1
	ldr	r3, .L58+16
	ldr	r3, [r3]
	ldrb	r3, [r3, #2]
	strb	r3, [sp, #39]
	.loc 4 43 17
	ldr	r3, .L58+16
	ldr	r3, [r3]
	ldrb	r3, [r3, #1]
	strb	r3, [sp, #38]
	.loc 4 44 44
	ldrb	r2, [sp, #39]	@ zero_extendqisi2
	.loc 4 44 51
	ldrb	r3, [sp, #38]	@ zero_extendqisi2
	lsls	r3, r3, #4
	.loc 4 44 44
	add	r3, r3, r2
	.loc 4 44 18
	str	r3, [sp, #32]
	.loc 4 45 9
	ldr	r3, .L58+16
	ldr	r3, [r3]
	ldr	r1, [sp, #32]
	mov	r0, r3
	bl	spis_setfrom_master
	.loc 4 46 21
	ldr	r3, .L58+16
	ldr	r3, [r3]
	ldrb	r3, [r3]	@ zero_extendqisi2
	.loc 4 46 12
	cmp	r3, #0
	beq	.L57
	.loc 4 48 24
	ldr	r3, .L58+24
	movs	r2, #0
	strb	r2, [r3]
.L57:
.LBE2:
	.loc 4 51 1
	nop
	add	sp, sp, #40
.LCFI2:
	@ sp needed
	pop	{r4, pc}
.L59:
	.align	2
.L58:
	.word	spis_xfer_done
	.word	g_log_dbg_msk
	.word	g_log_dbg_lvl
	.word	.LC1+80
	.word	m_rx_buf
	.word	.LC2
	.word	SWITCH2SPI
.LFE287:
	.size	spis_event_handler, .-spis_event_handler
	.section .rodata
	.align	2
.LC3:
	.ascii	"spis_start\012\000"
	.align	2
.LC4:
	.ascii	"tx_data.tx_data_buf: %s, addr: %x\012\000"
	.align	2
.LC0:
	.word	255
	.word	255
	.word	255
	.word	255
	.byte	0
	.byte	0
	.byte	0
	.byte	0
	.byte	-1
	.byte	-1
	.byte	6
	.space	1
	.section	.text.spis_start,"ax",%progbits
	.align	1
	.global	spis_start
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	spis_start, %function
spis_start:
.LFB288:
	.loc 4 54 1
	@ args = 0, pretend = 0, frame = 48
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, lr}
.LCFI3:
	sub	sp, sp, #68
.LCFI4:
	.loc 4 59 5
	ldr	r3, .L74
	ldr	r3, [r3]
	and	r3, r3, #16384
	cmp	r3, #0
	beq	.L61
	.loc 4 59 5 is_stmt 0 discriminator 1
	ldr	r3, .L74+4
	ldr	r3, [r3]
	cmp	r3, #3
	ble	.L61
	.loc 4 59 5 discriminator 2
	ldr	r4, .L74+8
	bl	log_timestamp_get
	mov	r3, r0
	ldr	r2, .L74+12
	str	r2, [sp]
	movs	r2, #59
	mov	r1, r4
	movs	r0, #4
	bl	log_printf
.L61:
	.loc 4 66 25 is_stmt 1
	add	r3, sp, #44
	mov	r0, r3
	bl	spis_getfrom_slave
	.loc 4 67 29
	movs	r3, #100
	mov	r0, r3
	bl	malloc
	mov	r3, r0
	mov	r2, r3
	.loc 4 67 15
	ldr	r3, .L74+16
	str	r2, [r3]
	.loc 4 68 19
	ldr	r3, .L74+16
	ldr	r3, [r3]
	.loc 4 68 9
	cmp	r3, #0
	beq	.L73
	.loc 4 72 6
	ldr	r3, .L74
	ldr	r3, [r3]
	and	r3, r3, #16384
	cmp	r3, #0
	beq	.L64
	.loc 4 72 6 is_stmt 0 discriminator 1
	ldr	r3, .L74+4
	ldr	r3, [r3]
	cmp	r3, #3
	ble	.L64
	.loc 4 72 6 discriminator 2
	ldr	r4, .L74+8
	bl	log_timestamp_get
	mov	r1, r0
	ldr	r3, [sp, #44]
	ldr	r2, [sp, #44]
	str	r2, [sp, #8]
	str	r3, [sp, #4]
	ldr	r3, .L74+20
	str	r3, [sp]
	mov	r3, r1
	movs	r2, #72
	mov	r1, r4
	movs	r0, #4
	bl	log_printf
.L64:
	.loc 4 75 27 is_stmt 1
	ldr	r3, [sp, #48]
	.loc 4 75 18
	ldr	r2, .L74+24
	str	r3, [r2]
.LBB3:
	.loc 4 76 20
	movs	r3, #0
	str	r3, [sp, #60]
	.loc 4 76 6
	b	.L65
.L66:
	.loc 4 78 31 discriminator 3
	ldr	r2, [sp, #44]
	.loc 4 78 43 discriminator 3
	ldr	r3, [sp, #60]
	add	r2, r2, r3
	.loc 4 78 18 discriminator 3
	ldr	r3, .L74+16
	ldr	r1, [r3]
	ldr	r3, [sp, #60]
	add	r3, r3, r1
	.loc 4 78 43 discriminator 3
	ldrb	r2, [r2]	@ zero_extendqisi2
	.loc 4 78 22 discriminator 3
	strb	r2, [r3]
	.loc 4 76 45 discriminator 3
	ldr	r3, [sp, #60]
	adds	r3, r3, #1
	str	r3, [sp, #60]
.L65:
	.loc 4 76 29 discriminator 1
	ldr	r3, .L74+24
	ldr	r3, [r3]
	.loc 4 76 6 discriminator 1
	ldr	r2, [sp, #60]
	cmp	r2, r3
	bcc	.L66
.LBE3:
	.loc 4 82 27
	ldr	r3, .L74+28
	add	r4, sp, #20
	mov	r5, r3
	ldmia	r5!, {r0, r1, r2, r3}
	stmia	r4!, {r0, r1, r2, r3}
	ldm	r5, {r0, r1}
	stm	r4, {r0, r1}
	.loc 4 83 39
	movs	r3, #31
	str	r3, [sp, #32]
	.loc 4 84 39
	movs	r3, #30
	str	r3, [sp, #20]
	.loc 4 85 39
	movs	r3, #29
	str	r3, [sp, #24]
	.loc 4 86 39
	movs	r3, #26
	str	r3, [sp, #28]
.LBB4:
	.loc 4 89 5
	add	r3, sp, #20
	ldr	r2, .L74+32
	mov	r1, r3
	ldr	r0, .L74+36
	bl	nrf_drv_spis_init
	str	r0, [sp, #56]
	ldr	r3, [sp, #56]
	cmp	r3, #0
	beq	.L68
	.loc 4 89 5 is_stmt 0 discriminator 1
	ldr	r0, [sp, #56]
	bl	app_error_handler_bare
.LBE4:
	.loc 4 91 11 is_stmt 1 discriminator 1
	b	.L68
.L72:
	.loc 4 93 32
	movs	r3, #100
	mov	r0, r3
	bl	malloc
	mov	r3, r0
	mov	r2, r3
	.loc 4 93 18
	ldr	r3, .L74+40
	str	r2, [r3]
	.loc 4 94 9
	ldr	r3, .L74+40
	ldr	r3, [r3]
	movs	r2, #100
	movs	r1, #0
	mov	r0, r3
	bl	memset
	.loc 4 96 24
	ldr	r3, .L74+44
	movs	r2, #0
	strb	r2, [r3]
.LBB5:
	.loc 4 97 9
	ldr	r3, .L74+16
	ldr	r1, [r3]
	ldr	r3, .L74+24
	ldr	r2, [r3]
	ldr	r3, .L74+40
	ldr	r3, [r3]
	movs	r0, #100
	str	r0, [sp]
	ldr	r0, .L74+36
	bl	nrfx_spis_buffers_set
	str	r0, [sp, #52]
	ldr	r3, [sp, #52]
	cmp	r3, #0
	beq	.L70
	.loc 4 97 9 is_stmt 0 discriminator 1
	ldr	r0, [sp, #52]
	bl	app_error_handler_bare
.LBE5:
	.loc 4 98 15 is_stmt 1 discriminator 1
	b	.L70
.L71:
	.loc 4 101 19
	bl	sd_app_evt_wait
	.loc 4 102 13
	movs	r0, #0
	bl	bsp_board_led_invert
.L70:
	.loc 4 98 16
	ldr	r3, .L74+44
	ldrb	r3, [r3]
	uxtb	r3, r3
	eor	r3, r3, #1
	uxtb	r3, r3
	.loc 4 98 15
	cmp	r3, #0
	bne	.L71
.L68:
	.loc 4 91 12
	ldr	r3, .L74+48
	ldrsb	r3, [r3]
	.loc 4 91 11
	cmp	r3, #0
	bne	.L72
	b	.L60
.L73:
	.loc 4 70 10
	nop
.L60:
	.loc 4 106 1
	add	sp, sp, #68
.LCFI5:
	@ sp needed
	pop	{r4, r5, pc}
.L75:
	.align	2
.L74:
	.word	g_log_dbg_msk
	.word	g_log_dbg_lvl
	.word	.LC1+80
	.word	.LC3
	.word	m_tx_buf
	.word	.LC4
	.word	m_tx_length
	.word	.LC0
	.word	spis_event_handler
	.word	spis
	.word	m_rx_buf
	.word	spis_xfer_done
	.word	SWITCH2SPI
.LFE288:
	.size	spis_start, .-spis_start
	.section	.debug_frame,"",%progbits
.Lframe0:
	.4byte	.LECIE0-.LSCIE0
.LSCIE0:
	.4byte	0xffffffff
	.byte	0x3
	.ascii	"\000"
	.uleb128 0x1
	.sleb128 -4
	.uleb128 0xe
	.byte	0xc
	.uleb128 0xd
	.uleb128 0
	.align	2
.LECIE0:
.LSFDE0:
	.4byte	.LEFDE0-.LASFDE0
.LASFDE0:
	.4byte	.Lframe0
	.4byte	.LFB138
	.4byte	.LFE138-.LFB138
	.align	2
.LEFDE0:
.LSFDE2:
	.4byte	.LEFDE2-.LASFDE2
.LASFDE2:
	.4byte	.Lframe0
	.4byte	.LFB164
	.4byte	.LFE164-.LFB164
	.align	2
.LEFDE2:
.LSFDE4:
	.4byte	.LEFDE4-.LASFDE4
.LASFDE4:
	.4byte	.Lframe0
	.4byte	.LFB165
	.4byte	.LFE165-.LFB165
	.align	2
.LEFDE4:
.LSFDE6:
	.4byte	.LEFDE6-.LASFDE6
.LASFDE6:
	.4byte	.Lframe0
	.4byte	.LFB166
	.4byte	.LFE166-.LFB166
	.align	2
.LEFDE6:
.LSFDE8:
	.4byte	.LEFDE8-.LASFDE8
.LASFDE8:
	.4byte	.Lframe0
	.4byte	.LFB167
	.4byte	.LFE167-.LFB167
	.align	2
.LEFDE8:
.LSFDE10:
	.4byte	.LEFDE10-.LASFDE10
.LASFDE10:
	.4byte	.Lframe0
	.4byte	.LFB168
	.4byte	.LFE168-.LFB168
	.align	2
.LEFDE10:
.LSFDE12:
	.4byte	.LEFDE12-.LASFDE12
.LASFDE12:
	.4byte	.Lframe0
	.4byte	.LFB169
	.4byte	.LFE169-.LFB169
	.align	2
.LEFDE12:
.LSFDE14:
	.4byte	.LEFDE14-.LASFDE14
.LASFDE14:
	.4byte	.Lframe0
	.4byte	.LFB170
	.4byte	.LFE170-.LFB170
	.align	2
.LEFDE14:
.LSFDE16:
	.4byte	.LEFDE16-.LASFDE16
.LASFDE16:
	.4byte	.Lframe0
	.4byte	.LFB171
	.4byte	.LFE171-.LFB171
	.align	2
.LEFDE16:
.LSFDE18:
	.4byte	.LEFDE18-.LASFDE18
.LASFDE18:
	.4byte	.Lframe0
	.4byte	.LFB172
	.4byte	.LFE172-.LFB172
	.align	2
.LEFDE18:
.LSFDE20:
	.4byte	.LEFDE20-.LASFDE20
.LASFDE20:
	.4byte	.Lframe0
	.4byte	.LFB173
	.4byte	.LFE173-.LFB173
	.align	2
.LEFDE20:
.LSFDE22:
	.4byte	.LEFDE22-.LASFDE22
.LASFDE22:
	.4byte	.Lframe0
	.4byte	.LFB174
	.4byte	.LFE174-.LFB174
	.align	2
.LEFDE22:
.LSFDE24:
	.4byte	.LEFDE24-.LASFDE24
.LASFDE24:
	.4byte	.Lframe0
	.4byte	.LFB175
	.4byte	.LFE175-.LFB175
	.align	2
.LEFDE24:
.LSFDE26:
	.4byte	.LEFDE26-.LASFDE26
.LASFDE26:
	.4byte	.Lframe0
	.4byte	.LFB176
	.4byte	.LFE176-.LFB176
	.align	2
.LEFDE26:
.LSFDE28:
	.4byte	.LEFDE28-.LASFDE28
.LASFDE28:
	.4byte	.Lframe0
	.4byte	.LFB177
	.4byte	.LFE177-.LFB177
	.align	2
.LEFDE28:
.LSFDE30:
	.4byte	.LEFDE30-.LASFDE30
.LASFDE30:
	.4byte	.Lframe0
	.4byte	.LFB178
	.4byte	.LFE178-.LFB178
	.align	2
.LEFDE30:
.LSFDE32:
	.4byte	.LEFDE32-.LASFDE32
.LASFDE32:
	.4byte	.Lframe0
	.4byte	.LFB179
	.4byte	.LFE179-.LFB179
	.align	2
.LEFDE32:
.LSFDE34:
	.4byte	.LEFDE34-.LASFDE34
.LASFDE34:
	.4byte	.Lframe0
	.4byte	.LFB180
	.4byte	.LFE180-.LFB180
	.align	2
.LEFDE34:
.LSFDE36:
	.4byte	.LEFDE36-.LASFDE36
.LASFDE36:
	.4byte	.Lframe0
	.4byte	.LFB181
	.4byte	.LFE181-.LFB181
	.align	2
.LEFDE36:
.LSFDE38:
	.4byte	.LEFDE38-.LASFDE38
.LASFDE38:
	.4byte	.Lframe0
	.4byte	.LFB182
	.4byte	.LFE182-.LFB182
	.align	2
.LEFDE38:
.LSFDE40:
	.4byte	.LEFDE40-.LASFDE40
.LASFDE40:
	.4byte	.Lframe0
	.4byte	.LFB183
	.4byte	.LFE183-.LFB183
	.align	2
.LEFDE40:
.LSFDE42:
	.4byte	.LEFDE42-.LASFDE42
.LASFDE42:
	.4byte	.Lframe0
	.4byte	.LFB184
	.4byte	.LFE184-.LFB184
	.align	2
.LEFDE42:
.LSFDE44:
	.4byte	.LEFDE44-.LASFDE44
.LASFDE44:
	.4byte	.Lframe0
	.4byte	.LFB185
	.4byte	.LFE185-.LFB185
	.align	2
.LEFDE44:
.LSFDE46:
	.4byte	.LEFDE46-.LASFDE46
.LASFDE46:
	.4byte	.Lframe0
	.4byte	.LFB186
	.4byte	.LFE186-.LFB186
	.align	2
.LEFDE46:
.LSFDE48:
	.4byte	.LEFDE48-.LASFDE48
.LASFDE48:
	.4byte	.Lframe0
	.4byte	.LFB187
	.4byte	.LFE187-.LFB187
	.align	2
.LEFDE48:
.LSFDE50:
	.4byte	.LEFDE50-.LASFDE50
.LASFDE50:
	.4byte	.Lframe0
	.4byte	.LFB188
	.4byte	.LFE188-.LFB188
	.align	2
.LEFDE50:
.LSFDE52:
	.4byte	.LEFDE52-.LASFDE52
.LASFDE52:
	.4byte	.Lframe0
	.4byte	.LFB189
	.4byte	.LFE189-.LFB189
	.align	2
.LEFDE52:
.LSFDE54:
	.4byte	.LEFDE54-.LASFDE54
.LASFDE54:
	.4byte	.Lframe0
	.4byte	.LFB190
	.4byte	.LFE190-.LFB190
	.align	2
.LEFDE54:
.LSFDE56:
	.4byte	.LEFDE56-.LASFDE56
.LASFDE56:
	.4byte	.Lframe0
	.4byte	.LFB191
	.4byte	.LFE191-.LFB191
	.align	2
.LEFDE56:
.LSFDE58:
	.4byte	.LEFDE58-.LASFDE58
.LASFDE58:
	.4byte	.Lframe0
	.4byte	.LFB192
	.4byte	.LFE192-.LFB192
	.align	2
.LEFDE58:
.LSFDE60:
	.4byte	.LEFDE60-.LASFDE60
.LASFDE60:
	.4byte	.Lframe0
	.4byte	.LFB193
	.4byte	.LFE193-.LFB193
	.align	2
.LEFDE60:
.LSFDE62:
	.4byte	.LEFDE62-.LASFDE62
.LASFDE62:
	.4byte	.Lframe0
	.4byte	.LFB194
	.4byte	.LFE194-.LFB194
	.align	2
.LEFDE62:
.LSFDE64:
	.4byte	.LEFDE64-.LASFDE64
.LASFDE64:
	.4byte	.Lframe0
	.4byte	.LFB195
	.4byte	.LFE195-.LFB195
	.align	2
.LEFDE64:
.LSFDE66:
	.4byte	.LEFDE66-.LASFDE66
.LASFDE66:
	.4byte	.Lframe0
	.4byte	.LFB196
	.4byte	.LFE196-.LFB196
	.align	2
.LEFDE66:
.LSFDE68:
	.4byte	.LEFDE68-.LASFDE68
.LASFDE68:
	.4byte	.Lframe0
	.4byte	.LFB197
	.4byte	.LFE197-.LFB197
	.align	2
.LEFDE68:
.LSFDE70:
	.4byte	.LEFDE70-.LASFDE70
.LASFDE70:
	.4byte	.Lframe0
	.4byte	.LFB198
	.4byte	.LFE198-.LFB198
	.align	2
.LEFDE70:
.LSFDE72:
	.4byte	.LEFDE72-.LASFDE72
.LASFDE72:
	.4byte	.Lframe0
	.4byte	.LFB199
	.4byte	.LFE199-.LFB199
	.align	2
.LEFDE72:
.LSFDE74:
	.4byte	.LEFDE74-.LASFDE74
.LASFDE74:
	.4byte	.Lframe0
	.4byte	.LFB200
	.4byte	.LFE200-.LFB200
	.align	2
.LEFDE74:
.LSFDE76:
	.4byte	.LEFDE76-.LASFDE76
.LASFDE76:
	.4byte	.Lframe0
	.4byte	.LFB201
	.4byte	.LFE201-.LFB201
	.align	2
.LEFDE76:
.LSFDE78:
	.4byte	.LEFDE78-.LASFDE78
.LASFDE78:
	.4byte	.Lframe0
	.4byte	.LFB202
	.4byte	.LFE202-.LFB202
	.align	2
.LEFDE78:
.LSFDE80:
	.4byte	.LEFDE80-.LASFDE80
.LASFDE80:
	.4byte	.Lframe0
	.4byte	.LFB203
	.4byte	.LFE203-.LFB203
	.align	2
.LEFDE80:
.LSFDE82:
	.4byte	.LEFDE82-.LASFDE82
.LASFDE82:
	.4byte	.Lframe0
	.4byte	.LFB204
	.4byte	.LFE204-.LFB204
	.align	2
.LEFDE82:
.LSFDE84:
	.4byte	.LEFDE84-.LASFDE84
.LASFDE84:
	.4byte	.Lframe0
	.4byte	.LFB205
	.4byte	.LFE205-.LFB205
	.align	2
.LEFDE84:
.LSFDE86:
	.4byte	.LEFDE86-.LASFDE86
.LASFDE86:
	.4byte	.Lframe0
	.4byte	.LFB206
	.4byte	.LFE206-.LFB206
	.align	2
.LEFDE86:
.LSFDE88:
	.4byte	.LEFDE88-.LASFDE88
.LASFDE88:
	.4byte	.Lframe0
	.4byte	.LFB207
	.4byte	.LFE207-.LFB207
	.align	2
.LEFDE88:
.LSFDE90:
	.4byte	.LEFDE90-.LASFDE90
.LASFDE90:
	.4byte	.Lframe0
	.4byte	.LFB208
	.4byte	.LFE208-.LFB208
	.align	2
.LEFDE90:
.LSFDE92:
	.4byte	.LEFDE92-.LASFDE92
.LASFDE92:
	.4byte	.Lframe0
	.4byte	.LFB209
	.4byte	.LFE209-.LFB209
	.align	2
.LEFDE92:
.LSFDE94:
	.4byte	.LEFDE94-.LASFDE94
.LASFDE94:
	.4byte	.Lframe0
	.4byte	.LFB210
	.4byte	.LFE210-.LFB210
	.align	2
.LEFDE94:
.LSFDE96:
	.4byte	.LEFDE96-.LASFDE96
.LASFDE96:
	.4byte	.Lframe0
	.4byte	.LFB211
	.4byte	.LFE211-.LFB211
	.align	2
.LEFDE96:
.LSFDE98:
	.4byte	.LEFDE98-.LASFDE98
.LASFDE98:
	.4byte	.Lframe0
	.4byte	.LFB286
	.4byte	.LFE286-.LFB286
	.align	2
.LEFDE98:
.LSFDE100:
	.4byte	.LEFDE100-.LASFDE100
.LASFDE100:
	.4byte	.Lframe0
	.4byte	.LFB287
	.4byte	.LFE287-.LFB287
	.byte	0x4
	.4byte	.LCFI0-.LFB287
	.byte	0xe
	.uleb128 0x8
	.byte	0x84
	.uleb128 0x2
	.byte	0x8e
	.uleb128 0x1
	.byte	0x4
	.4byte	.LCFI1-.LCFI0
	.byte	0xe
	.uleb128 0x30
	.byte	0x4
	.4byte	.LCFI2-.LCFI1
	.byte	0xe
	.uleb128 0x8
	.align	2
.LEFDE100:
.LSFDE102:
	.4byte	.LEFDE102-.LASFDE102
.LASFDE102:
	.4byte	.Lframe0
	.4byte	.LFB288
	.4byte	.LFE288-.LFB288
	.byte	0x4
	.4byte	.LCFI3-.LFB288
	.byte	0xe
	.uleb128 0xc
	.byte	0x84
	.uleb128 0x3
	.byte	0x85
	.uleb128 0x2
	.byte	0x8e
	.uleb128 0x1
	.byte	0x4
	.4byte	.LCFI4-.LCFI3
	.byte	0xe
	.uleb128 0x50
	.byte	0x4
	.4byte	.LCFI5-.LCFI4
	.byte	0xe
	.uleb128 0xc
	.align	2
.LEFDE102:
	.text
.Letext0:
	.file 5 "/usr/share/segger_embedded_studio_for_arm_5.62/include/string.h"
	.file 6 "/usr/share/segger_embedded_studio_for_arm_5.62/include/stdint.h"
	.file 7 "../../../nRF5_SDK_17.0.2_d674dde/modules/nrfx/mdk/nrf52840.h"
	.file 8 "../../../nRF5_SDK_17.0.2_d674dde/modules/nrfx/hal/nrf_spis.h"
	.file 9 "../../../nRF5_SDK_17.0.2_d674dde/modules/nrfx/hal/nrf_gpio.h"
	.file 10 "../../../nRF5_SDK_17.0.2_d674dde/modules/nrfx/drivers/include/nrfx_spis.h"
	.file 11 "../../../nRF5_SDK_17.0.2_d674dde/integration/nrfx/legacy/nrf_drv_spis.h"
	.file 12 "include/spis.h"
	.file 13 "include/spis_data.h"
	.section	.debug_info,"",%progbits
.Ldebug_info0:
	.4byte	0x194b
	.2byte	0x4
	.4byte	.Ldebug_abbrev0
	.byte	0x4
	.uleb128 0x1
	.4byte	.LASF332
	.byte	0xc
	.4byte	.LASF333
	.4byte	.LASF334
	.4byte	.Ldebug_ranges0+0
	.4byte	0
	.4byte	.Ldebug_line0
	.uleb128 0x2
	.byte	0x4
	.byte	0x5
	.ascii	"int\000"
	.uleb128 0x3
	.byte	0x4
	.byte	0x5
	.4byte	.LASF0
	.uleb128 0x3
	.byte	0x1
	.byte	0x8
	.4byte	.LASF1
	.uleb128 0x3
	.byte	0x4
	.byte	0x7
	.4byte	.LASF2
	.uleb128 0x3
	.byte	0x1
	.byte	0x8
	.4byte	.LASF3
	.uleb128 0x3
	.byte	0x2
	.byte	0x7
	.4byte	.LASF4
	.uleb128 0x4
	.4byte	.LASF6
	.byte	0x5
	.byte	0x31
	.byte	0x16
	.4byte	0x3a
	.uleb128 0x3
	.byte	0x8
	.byte	0x5
	.4byte	.LASF5
	.uleb128 0x4
	.4byte	.LASF7
	.byte	0x6
	.byte	0x29
	.byte	0x1c
	.4byte	0x6e
	.uleb128 0x3
	.byte	0x1
	.byte	0x6
	.4byte	.LASF8
	.uleb128 0x4
	.4byte	.LASF9
	.byte	0x6
	.byte	0x2a
	.byte	0x1c
	.4byte	0x41
	.uleb128 0x5
	.4byte	0x75
	.uleb128 0x3
	.byte	0x2
	.byte	0x5
	.4byte	.LASF10
	.uleb128 0x4
	.4byte	.LASF11
	.byte	0x6
	.byte	0x36
	.byte	0x1c
	.4byte	0x25
	.uleb128 0x4
	.4byte	.LASF12
	.byte	0x6
	.byte	0x37
	.byte	0x1c
	.4byte	0x3a
	.uleb128 0x5
	.4byte	0x99
	.uleb128 0x6
	.4byte	0xa5
	.uleb128 0x6
	.4byte	0x99
	.uleb128 0x3
	.byte	0x8
	.byte	0x7
	.4byte	.LASF13
	.uleb128 0x3
	.byte	0x8
	.byte	0x4
	.4byte	.LASF14
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0xd2
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x1
	.byte	0
	.uleb128 0x6
	.4byte	0xc2
	.uleb128 0x5
	.4byte	0xd2
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0xec
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x4
	.byte	0
	.uleb128 0x6
	.4byte	0xdc
	.uleb128 0x5
	.4byte	0xec
	.uleb128 0x9
	.byte	0x10
	.byte	0x7
	.2byte	0x182
	.byte	0x9
	.4byte	0x139
	.uleb128 0xa
	.ascii	"SCK\000"
	.byte	0x7
	.2byte	0x183
	.byte	0x13
	.4byte	0xa5
	.byte	0
	.uleb128 0xb
	.4byte	.LASF15
	.byte	0x7
	.2byte	0x184
	.byte	0x13
	.4byte	0xa5
	.byte	0x4
	.uleb128 0xb
	.4byte	.LASF16
	.byte	0x7
	.2byte	0x185
	.byte	0x13
	.4byte	0xa5
	.byte	0x8
	.uleb128 0xa
	.ascii	"CSN\000"
	.byte	0x7
	.2byte	0x186
	.byte	0x13
	.4byte	0xa5
	.byte	0xc
	.byte	0
	.uleb128 0xc
	.4byte	.LASF17
	.byte	0x7
	.2byte	0x187
	.byte	0x3
	.4byte	0xf6
	.uleb128 0x5
	.4byte	0x139
	.uleb128 0x9
	.byte	0x10
	.byte	0x7
	.2byte	0x18d
	.byte	0x9
	.4byte	0x18e
	.uleb128 0xa
	.ascii	"PTR\000"
	.byte	0x7
	.2byte	0x18e
	.byte	0x13
	.4byte	0xa5
	.byte	0
	.uleb128 0xb
	.4byte	.LASF18
	.byte	0x7
	.2byte	0x18f
	.byte	0x13
	.4byte	0xa5
	.byte	0x4
	.uleb128 0xb
	.4byte	.LASF19
	.byte	0x7
	.2byte	0x190
	.byte	0x13
	.4byte	0xaa
	.byte	0x8
	.uleb128 0xb
	.4byte	.LASF20
	.byte	0x7
	.2byte	0x191
	.byte	0x13
	.4byte	0xa5
	.byte	0xc
	.byte	0
	.uleb128 0xc
	.4byte	.LASF21
	.byte	0x7
	.2byte	0x192
	.byte	0x3
	.4byte	0x14b
	.uleb128 0x5
	.4byte	0x18e
	.uleb128 0x9
	.byte	0x10
	.byte	0x7
	.2byte	0x198
	.byte	0x9
	.4byte	0x1e3
	.uleb128 0xa
	.ascii	"PTR\000"
	.byte	0x7
	.2byte	0x199
	.byte	0x13
	.4byte	0xa5
	.byte	0
	.uleb128 0xb
	.4byte	.LASF18
	.byte	0x7
	.2byte	0x19a
	.byte	0x13
	.4byte	0xa5
	.byte	0x4
	.uleb128 0xb
	.4byte	.LASF19
	.byte	0x7
	.2byte	0x19b
	.byte	0x13
	.4byte	0xaa
	.byte	0x8
	.uleb128 0xb
	.4byte	.LASF20
	.byte	0x7
	.2byte	0x19c
	.byte	0x13
	.4byte	0xa5
	.byte	0xc
	.byte	0
	.uleb128 0xc
	.4byte	.LASF22
	.byte	0x7
	.2byte	0x19d
	.byte	0x3
	.4byte	0x1a0
	.uleb128 0x5
	.4byte	0x1e3
	.uleb128 0x7
	.4byte	0xa5
	.4byte	0x205
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x3
	.byte	0
	.uleb128 0x5
	.4byte	0x1f5
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x21a
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x3f
	.byte	0
	.uleb128 0x6
	.4byte	0x20a
	.uleb128 0x5
	.4byte	0x21a
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x234
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x3b
	.byte	0
	.uleb128 0x6
	.4byte	0x224
	.uleb128 0x5
	.4byte	0x234
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x24e
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x3c
	.byte	0
	.uleb128 0x6
	.4byte	0x23e
	.uleb128 0x5
	.4byte	0x24e
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x268
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x8
	.byte	0
	.uleb128 0x6
	.4byte	0x258
	.uleb128 0x5
	.4byte	0x268
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x282
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x2e
	.byte	0
	.uleb128 0x6
	.4byte	0x272
	.uleb128 0x5
	.4byte	0x282
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x29c
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x6
	.byte	0
	.uleb128 0x6
	.4byte	0x28c
	.uleb128 0x5
	.4byte	0x29c
	.uleb128 0xd
	.2byte	0x5c4
	.byte	0x7
	.2byte	0x58a
	.byte	0x9
	.4byte	0x470
	.uleb128 0xb
	.4byte	.LASF23
	.byte	0x7
	.2byte	0x58b
	.byte	0x13
	.4byte	0x26d
	.byte	0
	.uleb128 0xb
	.4byte	.LASF24
	.byte	0x7
	.2byte	0x58c
	.byte	0x13
	.4byte	0xa5
	.byte	0x24
	.uleb128 0xb
	.4byte	.LASF25
	.byte	0x7
	.2byte	0x58d
	.byte	0x13
	.4byte	0xa5
	.byte	0x28
	.uleb128 0xb
	.4byte	.LASF26
	.byte	0x7
	.2byte	0x58f
	.byte	0x13
	.4byte	0x485
	.byte	0x2c
	.uleb128 0xe
	.4byte	.LASF27
	.byte	0x7
	.2byte	0x590
	.byte	0x13
	.4byte	0xa5
	.2byte	0x104
	.uleb128 0xe
	.4byte	.LASF28
	.byte	0x7
	.2byte	0x591
	.byte	0x13
	.4byte	0xd7
	.2byte	0x108
	.uleb128 0xe
	.4byte	.LASF29
	.byte	0x7
	.2byte	0x592
	.byte	0x13
	.4byte	0xa5
	.2byte	0x110
	.uleb128 0xe
	.4byte	.LASF30
	.byte	0x7
	.2byte	0x593
	.byte	0x13
	.4byte	0xf1
	.2byte	0x114
	.uleb128 0xe
	.4byte	.LASF31
	.byte	0x7
	.2byte	0x594
	.byte	0x13
	.4byte	0xa5
	.2byte	0x128
	.uleb128 0xe
	.4byte	.LASF32
	.byte	0x7
	.2byte	0x595
	.byte	0x13
	.4byte	0x49f
	.2byte	0x12c
	.uleb128 0xe
	.4byte	.LASF33
	.byte	0x7
	.2byte	0x596
	.byte	0x13
	.4byte	0xa5
	.2byte	0x200
	.uleb128 0xe
	.4byte	.LASF34
	.byte	0x7
	.2byte	0x597
	.byte	0x13
	.4byte	0x21f
	.2byte	0x204
	.uleb128 0xe
	.4byte	.LASF35
	.byte	0x7
	.2byte	0x598
	.byte	0x13
	.4byte	0xa5
	.2byte	0x304
	.uleb128 0xe
	.4byte	.LASF36
	.byte	0x7
	.2byte	0x599
	.byte	0x13
	.4byte	0xa5
	.2byte	0x308
	.uleb128 0xe
	.4byte	.LASF37
	.byte	0x7
	.2byte	0x59a
	.byte	0x13
	.4byte	0x253
	.2byte	0x30c
	.uleb128 0xe
	.4byte	.LASF38
	.byte	0x7
	.2byte	0x59b
	.byte	0x13
	.4byte	0xaa
	.2byte	0x400
	.uleb128 0xe
	.4byte	.LASF39
	.byte	0x7
	.2byte	0x59c
	.byte	0x13
	.4byte	0x4b9
	.2byte	0x404
	.uleb128 0xe
	.4byte	.LASF40
	.byte	0x7
	.2byte	0x59d
	.byte	0x13
	.4byte	0xa5
	.2byte	0x440
	.uleb128 0xe
	.4byte	.LASF41
	.byte	0x7
	.2byte	0x59e
	.byte	0x13
	.4byte	0x287
	.2byte	0x444
	.uleb128 0xe
	.4byte	.LASF42
	.byte	0x7
	.2byte	0x59f
	.byte	0x13
	.4byte	0xa5
	.2byte	0x500
	.uleb128 0xe
	.4byte	.LASF43
	.byte	0x7
	.2byte	0x5a0
	.byte	0x13
	.4byte	0xaa
	.2byte	0x504
	.uleb128 0xe
	.4byte	.LASF44
	.byte	0x7
	.2byte	0x5a1
	.byte	0x18
	.4byte	0x146
	.2byte	0x508
	.uleb128 0xe
	.4byte	.LASF45
	.byte	0x7
	.2byte	0x5a2
	.byte	0x13
	.4byte	0x2a1
	.2byte	0x518
	.uleb128 0xf
	.ascii	"RXD\000"
	.byte	0x7
	.2byte	0x5a3
	.byte	0x17
	.4byte	0x19b
	.2byte	0x534
	.uleb128 0xf
	.ascii	"TXD\000"
	.byte	0x7
	.2byte	0x5a4
	.byte	0x17
	.4byte	0x1f0
	.2byte	0x544
	.uleb128 0xe
	.4byte	.LASF46
	.byte	0x7
	.2byte	0x5a5
	.byte	0x13
	.4byte	0xa5
	.2byte	0x554
	.uleb128 0xe
	.4byte	.LASF47
	.byte	0x7
	.2byte	0x5a6
	.byte	0x13
	.4byte	0xaa
	.2byte	0x558
	.uleb128 0xf
	.ascii	"DEF\000"
	.byte	0x7
	.2byte	0x5a7
	.byte	0x13
	.4byte	0xa5
	.2byte	0x55c
	.uleb128 0xe
	.4byte	.LASF48
	.byte	0x7
	.2byte	0x5a9
	.byte	0x13
	.4byte	0x4d3
	.2byte	0x560
	.uleb128 0xf
	.ascii	"ORC\000"
	.byte	0x7
	.2byte	0x5aa
	.byte	0x13
	.4byte	0xa5
	.2byte	0x5c0
	.byte	0
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x480
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x35
	.byte	0
	.uleb128 0x6
	.4byte	0x470
	.uleb128 0x5
	.4byte	0x480
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x49a
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x34
	.byte	0
	.uleb128 0x6
	.4byte	0x48a
	.uleb128 0x5
	.4byte	0x49a
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x4b4
	.uleb128 0x8
	.4byte	0x3a
	.byte	0xe
	.byte	0
	.uleb128 0x6
	.4byte	0x4a4
	.uleb128 0x5
	.4byte	0x4b4
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x4ce
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x17
	.byte	0
	.uleb128 0x6
	.4byte	0x4be
	.uleb128 0x5
	.4byte	0x4ce
	.uleb128 0xc
	.4byte	.LASF49
	.byte	0x7
	.2byte	0x5ab
	.byte	0x3
	.4byte	0x2a6
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x4f5
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x6d
	.byte	0
	.uleb128 0x6
	.4byte	0x4e5
	.uleb128 0x5
	.4byte	0x4f5
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x50f
	.uleb128 0x8
	.4byte	0x3a
	.byte	0xd
	.byte	0
	.uleb128 0x6
	.4byte	0x4ff
	.uleb128 0x5
	.4byte	0x50f
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x529
	.uleb128 0x8
	.4byte	0x3a
	.byte	0xc
	.byte	0
	.uleb128 0x6
	.4byte	0x519
	.uleb128 0x5
	.4byte	0x529
	.uleb128 0x5
	.4byte	0x529
	.uleb128 0xd
	.2byte	0x550
	.byte	0x7
	.2byte	0x735
	.byte	0x9
	.4byte	0x679
	.uleb128 0xb
	.4byte	.LASF50
	.byte	0x7
	.2byte	0x736
	.byte	0x13
	.4byte	0xa5
	.byte	0
	.uleb128 0xb
	.4byte	.LASF51
	.byte	0x7
	.2byte	0x737
	.byte	0x13
	.4byte	0xa5
	.byte	0x4
	.uleb128 0xb
	.4byte	.LASF52
	.byte	0x7
	.2byte	0x738
	.byte	0x13
	.4byte	0xa5
	.byte	0x8
	.uleb128 0xb
	.4byte	.LASF53
	.byte	0x7
	.2byte	0x739
	.byte	0x13
	.4byte	0xa5
	.byte	0xc
	.uleb128 0xb
	.4byte	.LASF23
	.byte	0x7
	.2byte	0x73a
	.byte	0x13
	.4byte	0x239
	.byte	0x10
	.uleb128 0xe
	.4byte	.LASF54
	.byte	0x7
	.2byte	0x73b
	.byte	0x13
	.4byte	0xa5
	.2byte	0x100
	.uleb128 0xe
	.4byte	.LASF55
	.byte	0x7
	.2byte	0x73c
	.byte	0x13
	.4byte	0xa5
	.2byte	0x104
	.uleb128 0xe
	.4byte	.LASF26
	.byte	0x7
	.2byte	0x73d
	.byte	0x13
	.4byte	0x514
	.2byte	0x108
	.uleb128 0xe
	.4byte	.LASF56
	.byte	0x7
	.2byte	0x73e
	.byte	0x13
	.4byte	0x205
	.2byte	0x140
	.uleb128 0xe
	.4byte	.LASF28
	.byte	0x7
	.2byte	0x740
	.byte	0x13
	.4byte	0x68e
	.2byte	0x150
	.uleb128 0xe
	.4byte	.LASF35
	.byte	0x7
	.2byte	0x741
	.byte	0x13
	.4byte	0xa5
	.2byte	0x304
	.uleb128 0xe
	.4byte	.LASF36
	.byte	0x7
	.2byte	0x742
	.byte	0x13
	.4byte	0xa5
	.2byte	0x308
	.uleb128 0xe
	.4byte	.LASF30
	.byte	0x7
	.2byte	0x743
	.byte	0x13
	.4byte	0x52e
	.2byte	0x30c
	.uleb128 0xe
	.4byte	.LASF57
	.byte	0x7
	.2byte	0x744
	.byte	0x13
	.4byte	0xa5
	.2byte	0x340
	.uleb128 0xe
	.4byte	.LASF58
	.byte	0x7
	.2byte	0x745
	.byte	0x13
	.4byte	0xa5
	.2byte	0x344
	.uleb128 0xe
	.4byte	.LASF59
	.byte	0x7
	.2byte	0x746
	.byte	0x13
	.4byte	0xa5
	.2byte	0x348
	.uleb128 0xe
	.4byte	.LASF32
	.byte	0x7
	.2byte	0x747
	.byte	0x13
	.4byte	0x4fa
	.2byte	0x34c
	.uleb128 0xe
	.4byte	.LASF60
	.byte	0x7
	.2byte	0x748
	.byte	0x13
	.4byte	0xaa
	.2byte	0x504
	.uleb128 0xe
	.4byte	.LASF61
	.byte	0x7
	.2byte	0x749
	.byte	0x13
	.4byte	0xa5
	.2byte	0x508
	.uleb128 0xe
	.4byte	.LASF34
	.byte	0x7
	.2byte	0x74b
	.byte	0x13
	.4byte	0x533
	.2byte	0x50c
	.uleb128 0xf
	.ascii	"CC\000"
	.byte	0x7
	.2byte	0x74c
	.byte	0x13
	.4byte	0x205
	.2byte	0x540
	.byte	0
	.uleb128 0x7
	.4byte	0xaa
	.4byte	0x689
	.uleb128 0x8
	.4byte	0x3a
	.byte	0x6c
	.byte	0
	.uleb128 0x6
	.4byte	0x679
	.uleb128 0x5
	.4byte	0x689
	.uleb128 0xc
	.4byte	.LASF62
	.byte	0x7
	.2byte	0x74d
	.byte	0x3
	.4byte	0x538
	.uleb128 0x10
	.byte	0x4
	.4byte	0x99
	.uleb128 0x11
	.4byte	.LASF81
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0x1
	.byte	0x59
	.byte	0x6
	.4byte	0x6bf
	.uleb128 0x12
	.4byte	.LASF83
	.byte	0x18
	.byte	0
	.uleb128 0x13
	.byte	0xc
	.byte	0x1
	.byte	0x7a
	.byte	0x9
	.4byte	0x6f0
	.uleb128 0x14
	.ascii	"src\000"
	.byte	0x1
	.byte	0x7c
	.byte	0xd
	.4byte	0x6a0
	.byte	0
	.uleb128 0x14
	.ascii	"dst\000"
	.byte	0x1
	.byte	0x7d
	.byte	0xd
	.4byte	0x6a0
	.byte	0x4
	.uleb128 0x14
	.ascii	"len\000"
	.byte	0x1
	.byte	0x7e
	.byte	0xc
	.4byte	0x99
	.byte	0x8
	.byte	0
	.uleb128 0x4
	.4byte	.LASF63
	.byte	0x1
	.byte	0x7f
	.byte	0x3
	.4byte	0x6bf
	.uleb128 0x13
	.byte	0xc
	.byte	0x1
	.byte	0x87
	.byte	0x9
	.4byte	0x72d
	.uleb128 0x15
	.4byte	.LASF64
	.byte	0x1
	.byte	0x89
	.byte	0xd
	.4byte	0x6a0
	.byte	0
	.uleb128 0x15
	.4byte	.LASF65
	.byte	0x1
	.byte	0x8a
	.byte	0xd
	.4byte	0x6a0
	.byte	0x4
	.uleb128 0x14
	.ascii	"len\000"
	.byte	0x1
	.byte	0x8b
	.byte	0xc
	.4byte	0x99
	.byte	0x8
	.byte	0
	.uleb128 0x4
	.4byte	.LASF66
	.byte	0x1
	.byte	0x8c
	.byte	0x3
	.4byte	0x6fc
	.uleb128 0x13
	.byte	0x8
	.byte	0x1
	.byte	0xa5
	.byte	0x9
	.4byte	0x75d
	.uleb128 0x15
	.4byte	.LASF67
	.byte	0x1
	.byte	0xa7
	.byte	0xd
	.4byte	0x6a0
	.byte	0
	.uleb128 0x15
	.4byte	.LASF68
	.byte	0x1
	.byte	0xa8
	.byte	0xc
	.4byte	0x99
	.byte	0x4
	.byte	0
	.uleb128 0x4
	.4byte	.LASF69
	.byte	0x1
	.byte	0xa9
	.byte	0x3
	.4byte	0x739
	.uleb128 0x13
	.byte	0x4
	.byte	0x1
	.byte	0xc1
	.byte	0x9
	.4byte	0x780
	.uleb128 0x15
	.4byte	.LASF70
	.byte	0x1
	.byte	0xc3
	.byte	0xc
	.4byte	0x99
	.byte	0
	.byte	0
	.uleb128 0x4
	.4byte	.LASF71
	.byte	0x1
	.byte	0xc4
	.byte	0x3
	.4byte	0x769
	.uleb128 0x13
	.byte	0x4
	.byte	0x1
	.byte	0xcd
	.byte	0x9
	.4byte	0x7a3
	.uleb128 0x15
	.4byte	.LASF70
	.byte	0x1
	.byte	0xcf
	.byte	0xc
	.4byte	0x99
	.byte	0
	.byte	0
	.uleb128 0x4
	.4byte	.LASF72
	.byte	0x1
	.byte	0xd0
	.byte	0x3
	.4byte	0x78c
	.uleb128 0x16
	.byte	0xc
	.byte	0x1
	.byte	0xdb
	.byte	0x3
	.4byte	0x7f5
	.uleb128 0x17
	.4byte	.LASF73
	.byte	0x1
	.byte	0xdd
	.byte	0x1e
	.4byte	0x6f0
	.uleb128 0x17
	.4byte	.LASF74
	.byte	0x1
	.byte	0xde
	.byte	0x1e
	.4byte	0x72d
	.uleb128 0x17
	.4byte	.LASF75
	.byte	0x1
	.byte	0xdf
	.byte	0x1e
	.4byte	0x75d
	.uleb128 0x17
	.4byte	.LASF76
	.byte	0x1
	.byte	0xe0
	.byte	0x2c
	.4byte	0x780
	.uleb128 0x17
	.4byte	.LASF77
	.byte	0x1
	.byte	0xe1
	.byte	0x2e
	.4byte	0x7a3
	.byte	0
	.uleb128 0x13
	.byte	0x10
	.byte	0x1
	.byte	0xd8
	.byte	0x9
	.4byte	0x819
	.uleb128 0x15
	.4byte	.LASF78
	.byte	0x1
	.byte	0xda
	.byte	0xc
	.4byte	0x99
	.byte	0
	.uleb128 0x15
	.4byte	.LASF79
	.byte	0x1
	.byte	0xe2
	.byte	0x5
	.4byte	0x7af
	.byte	0x4
	.byte	0
	.uleb128 0x4
	.4byte	.LASF80
	.byte	0x1
	.byte	0xe3
	.byte	0x3
	.4byte	0x7f5
	.uleb128 0x10
	.byte	0x4
	.4byte	0x75
	.uleb128 0x11
	.4byte	.LASF82
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0x2
	.byte	0x87
	.byte	0x6
	.4byte	0x964
	.uleb128 0x12
	.4byte	.LASF84
	.byte	0x20
	.uleb128 0x12
	.4byte	.LASF85
	.byte	0x21
	.uleb128 0x12
	.4byte	.LASF86
	.byte	0x22
	.uleb128 0x12
	.4byte	.LASF87
	.byte	0x23
	.uleb128 0x12
	.4byte	.LASF88
	.byte	0x24
	.uleb128 0x12
	.4byte	.LASF89
	.byte	0x25
	.uleb128 0x12
	.4byte	.LASF90
	.byte	0x26
	.uleb128 0x12
	.4byte	.LASF91
	.byte	0x27
	.uleb128 0x12
	.4byte	.LASF92
	.byte	0x28
	.uleb128 0x12
	.4byte	.LASF93
	.byte	0x29
	.uleb128 0x12
	.4byte	.LASF94
	.byte	0x2b
	.uleb128 0x12
	.4byte	.LASF95
	.byte	0x2c
	.uleb128 0x12
	.4byte	.LASF96
	.byte	0x2d
	.uleb128 0x12
	.4byte	.LASF97
	.byte	0x2e
	.uleb128 0x12
	.4byte	.LASF98
	.byte	0x2f
	.uleb128 0x12
	.4byte	.LASF99
	.byte	0x30
	.uleb128 0x12
	.4byte	.LASF100
	.byte	0x31
	.uleb128 0x12
	.4byte	.LASF101
	.byte	0x32
	.uleb128 0x12
	.4byte	.LASF102
	.byte	0x33
	.uleb128 0x12
	.4byte	.LASF103
	.byte	0x34
	.uleb128 0x12
	.4byte	.LASF104
	.byte	0x35
	.uleb128 0x12
	.4byte	.LASF105
	.byte	0x36
	.uleb128 0x12
	.4byte	.LASF106
	.byte	0x37
	.uleb128 0x12
	.4byte	.LASF107
	.byte	0x38
	.uleb128 0x12
	.4byte	.LASF108
	.byte	0x39
	.uleb128 0x12
	.4byte	.LASF109
	.byte	0x3a
	.uleb128 0x12
	.4byte	.LASF110
	.byte	0x3b
	.uleb128 0x12
	.4byte	.LASF111
	.byte	0x3c
	.uleb128 0x12
	.4byte	.LASF112
	.byte	0x3d
	.uleb128 0x12
	.4byte	.LASF113
	.byte	0x3e
	.uleb128 0x12
	.4byte	.LASF114
	.byte	0x3f
	.uleb128 0x12
	.4byte	.LASF115
	.byte	0x40
	.uleb128 0x12
	.4byte	.LASF116
	.byte	0x41
	.uleb128 0x12
	.4byte	.LASF117
	.byte	0x42
	.uleb128 0x12
	.4byte	.LASF118
	.byte	0x43
	.uleb128 0x12
	.4byte	.LASF119
	.byte	0x44
	.uleb128 0x12
	.4byte	.LASF120
	.byte	0x45
	.uleb128 0x12
	.4byte	.LASF121
	.byte	0x46
	.uleb128 0x12
	.4byte	.LASF122
	.byte	0x47
	.uleb128 0x12
	.4byte	.LASF123
	.byte	0x48
	.uleb128 0x12
	.4byte	.LASF124
	.byte	0x49
	.uleb128 0x12
	.4byte	.LASF125
	.byte	0x4a
	.uleb128 0x12
	.4byte	.LASF126
	.byte	0x4b
	.uleb128 0x12
	.4byte	.LASF127
	.byte	0x4c
	.uleb128 0x12
	.4byte	.LASF128
	.byte	0x4d
	.uleb128 0x12
	.4byte	.LASF129
	.byte	0x4e
	.uleb128 0x12
	.4byte	.LASF130
	.byte	0x4f
	.uleb128 0x12
	.4byte	.LASF131
	.byte	0x50
	.uleb128 0x12
	.4byte	.LASF132
	.byte	0x51
	.byte	0
	.uleb128 0xc
	.4byte	.LASF133
	.byte	0x2
	.2byte	0x165
	.byte	0x1a
	.4byte	0x81
	.uleb128 0x9
	.byte	0xc
	.byte	0x2
	.2byte	0x168
	.byte	0x9
	.4byte	0x9b4
	.uleb128 0xb
	.4byte	.LASF134
	.byte	0x2
	.2byte	0x16a
	.byte	0x11
	.4byte	0x75
	.byte	0
	.uleb128 0xb
	.4byte	.LASF135
	.byte	0x2
	.2byte	0x16b
	.byte	0x11
	.4byte	0x75
	.byte	0x1
	.uleb128 0xb
	.4byte	.LASF136
	.byte	0x2
	.2byte	0x16c
	.byte	0x11
	.4byte	0x99
	.byte	0x4
	.uleb128 0xb
	.4byte	.LASF137
	.byte	0x2
	.2byte	0x16d
	.byte	0x11
	.4byte	0x99
	.byte	0x8
	.byte	0
	.uleb128 0xc
	.4byte	.LASF138
	.byte	0x2
	.2byte	0x16e
	.byte	0x3
	.4byte	0x971
	.uleb128 0x9
	.byte	0xc
	.byte	0x2
	.2byte	0x171
	.byte	0x9
	.4byte	0xa04
	.uleb128 0xb
	.4byte	.LASF134
	.byte	0x2
	.2byte	0x173
	.byte	0x11
	.4byte	0x75
	.byte	0
	.uleb128 0xb
	.4byte	.LASF135
	.byte	0x2
	.2byte	0x174
	.byte	0x11
	.4byte	0x75
	.byte	0x1
	.uleb128 0xb
	.4byte	.LASF139
	.byte	0x2
	.2byte	0x175
	.byte	0x11
	.4byte	0x99
	.byte	0x4
	.uleb128 0xb
	.4byte	.LASF136
	.byte	0x2
	.2byte	0x176
	.byte	0x11
	.4byte	0x99
	.byte	0x8
	.byte	0
	.uleb128 0xc
	.4byte	.LASF140
	.byte	0x2
	.2byte	0x177
	.byte	0x3
	.4byte	0x9c1
	.uleb128 0x18
	.byte	0xc
	.byte	0x2
	.2byte	0x17d
	.byte	0x3
	.4byte	0xa36
	.uleb128 0x19
	.4byte	.LASF141
	.byte	0x2
	.2byte	0x17f
	.byte	0x23
	.4byte	0x9b4
	.uleb128 0x19
	.4byte	.LASF142
	.byte	0x2
	.2byte	0x180
	.byte	0x23
	.4byte	0xa04
	.byte	0
	.uleb128 0x9
	.byte	0x10
	.byte	0x2
	.2byte	0x17a
	.byte	0x9
	.4byte	0xa5d
	.uleb128 0xb
	.4byte	.LASF143
	.byte	0x2
	.2byte	0x17c
	.byte	0x23
	.4byte	0x75
	.byte	0
	.uleb128 0xb
	.4byte	.LASF79
	.byte	0x2
	.2byte	0x181
	.byte	0x5
	.4byte	0xa11
	.byte	0x4
	.byte	0
	.uleb128 0xc
	.4byte	.LASF144
	.byte	0x2
	.2byte	0x182
	.byte	0x3
	.4byte	0xa36
	.uleb128 0x6
	.4byte	0xa5d
	.uleb128 0x9
	.byte	0x4
	.byte	0x2
	.2byte	0x18a
	.byte	0x5
	.4byte	0xa88
	.uleb128 0xb
	.4byte	.LASF145
	.byte	0x2
	.2byte	0x18c
	.byte	0x1d
	.4byte	0xa88
	.byte	0
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xa5d
	.uleb128 0x9
	.byte	0x4
	.byte	0x2
	.2byte	0x18e
	.byte	0x5
	.4byte	0xaa7
	.uleb128 0xb
	.4byte	.LASF136
	.byte	0x2
	.2byte	0x190
	.byte	0x1d
	.4byte	0x99
	.byte	0
	.byte	0
	.uleb128 0x18
	.byte	0x4
	.byte	0x2
	.2byte	0x188
	.byte	0x3
	.4byte	0xacc
	.uleb128 0x19
	.4byte	.LASF146
	.byte	0x2
	.2byte	0x18d
	.byte	0x7
	.4byte	0xa6f
	.uleb128 0x19
	.4byte	.LASF147
	.byte	0x2
	.2byte	0x191
	.byte	0x7
	.4byte	0xa8e
	.byte	0
	.uleb128 0x9
	.byte	0x8
	.byte	0x2
	.2byte	0x185
	.byte	0x9
	.4byte	0xaf3
	.uleb128 0xb
	.4byte	.LASF148
	.byte	0x2
	.2byte	0x187
	.byte	0x19
	.4byte	0x75
	.byte	0
	.uleb128 0xb
	.4byte	.LASF79
	.byte	0x2
	.2byte	0x192
	.byte	0x5
	.4byte	0xaa7
	.byte	0x4
	.byte	0
	.uleb128 0xc
	.4byte	.LASF149
	.byte	0x2
	.2byte	0x193
	.byte	0x3
	.4byte	0xacc
	.uleb128 0xc
	.4byte	.LASF150
	.byte	0x2
	.2byte	0x1a1
	.byte	0x36
	.4byte	0xb0d
	.uleb128 0x10
	.byte	0x4
	.4byte	0xb13
	.uleb128 0x1a
	.4byte	0xb22
	.4byte	0xb22
	.uleb128 0x1b
	.4byte	0x75
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xaf3
	.uleb128 0xc
	.4byte	.LASF151
	.byte	0x2
	.2byte	0x1a4
	.byte	0x11
	.4byte	0xb35
	.uleb128 0x7
	.4byte	0x75
	.4byte	0xb45
	.uleb128 0x8
	.4byte	0x3a
	.byte	0xf
	.byte	0
	.uleb128 0xc
	.4byte	.LASF152
	.byte	0x2
	.2byte	0x1a5
	.byte	0x11
	.4byte	0xb35
	.uleb128 0xc
	.4byte	.LASF153
	.byte	0x2
	.2byte	0x1a6
	.byte	0x11
	.4byte	0xb35
	.uleb128 0x9
	.byte	0x30
	.byte	0x2
	.2byte	0x1a9
	.byte	0x9
	.4byte	0xb94
	.uleb128 0xa
	.ascii	"key\000"
	.byte	0x2
	.2byte	0x1ab
	.byte	0x18
	.4byte	0xb28
	.byte	0
	.uleb128 0xb
	.4byte	.LASF154
	.byte	0x2
	.2byte	0x1ac
	.byte	0x18
	.4byte	0xb45
	.byte	0x10
	.uleb128 0xb
	.4byte	.LASF155
	.byte	0x2
	.2byte	0x1ad
	.byte	0x18
	.4byte	0xb52
	.byte	0x20
	.byte	0
	.uleb128 0xc
	.4byte	.LASF156
	.byte	0x2
	.2byte	0x1ae
	.byte	0x3
	.4byte	0xb5f
	.uleb128 0x9
	.byte	0xc
	.byte	0x2
	.2byte	0x1b2
	.byte	0x9
	.4byte	0xbd6
	.uleb128 0xb
	.4byte	.LASF157
	.byte	0x2
	.2byte	0x1b4
	.byte	0x1f
	.4byte	0xbd6
	.byte	0
	.uleb128 0xb
	.4byte	.LASF158
	.byte	0x2
	.2byte	0x1b5
	.byte	0x1f
	.4byte	0xbdc
	.byte	0x4
	.uleb128 0xb
	.4byte	.LASF159
	.byte	0x2
	.2byte	0x1b6
	.byte	0x1f
	.4byte	0xbe2
	.byte	0x8
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xb35
	.uleb128 0x10
	.byte	0x4
	.4byte	0xb35
	.uleb128 0x10
	.byte	0x4
	.4byte	0xb52
	.uleb128 0xc
	.4byte	.LASF160
	.byte	0x2
	.2byte	0x1b7
	.byte	0x3
	.4byte	0xba1
	.uleb128 0x1c
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0x8
	.byte	0x5e
	.byte	0x1
	.4byte	0xc1c
	.uleb128 0x12
	.4byte	.LASF161
	.byte	0
	.uleb128 0x12
	.4byte	.LASF162
	.byte	0x1
	.uleb128 0x12
	.4byte	.LASF163
	.byte	0x2
	.uleb128 0x12
	.4byte	.LASF164
	.byte	0x3
	.byte	0
	.uleb128 0x4
	.4byte	.LASF165
	.byte	0x8
	.byte	0x63
	.byte	0x3
	.4byte	0xbf5
	.uleb128 0x1c
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0x8
	.byte	0x67
	.byte	0x1
	.4byte	0xc43
	.uleb128 0x12
	.4byte	.LASF166
	.byte	0
	.uleb128 0x12
	.4byte	.LASF167
	.byte	0x1
	.byte	0
	.uleb128 0x4
	.4byte	.LASF168
	.byte	0x8
	.byte	0x6a
	.byte	0x3
	.4byte	0xc28
	.uleb128 0x1c
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0x9
	.byte	0x67
	.byte	0x1
	.4byte	0xc70
	.uleb128 0x12
	.4byte	.LASF169
	.byte	0
	.uleb128 0x12
	.4byte	.LASF170
	.byte	0x1
	.uleb128 0x12
	.4byte	.LASF171
	.byte	0x3
	.byte	0
	.uleb128 0x4
	.4byte	.LASF172
	.byte	0x9
	.byte	0x6b
	.byte	0x3
	.4byte	0xc4f
	.uleb128 0x1c
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0x9
	.byte	0x6f
	.byte	0x1
	.4byte	0xcbb
	.uleb128 0x12
	.4byte	.LASF173
	.byte	0
	.uleb128 0x12
	.4byte	.LASF174
	.byte	0x1
	.uleb128 0x12
	.4byte	.LASF175
	.byte	0x2
	.uleb128 0x12
	.4byte	.LASF176
	.byte	0x3
	.uleb128 0x12
	.4byte	.LASF177
	.byte	0x4
	.uleb128 0x12
	.4byte	.LASF178
	.byte	0x5
	.uleb128 0x12
	.4byte	.LASF179
	.byte	0x6
	.uleb128 0x12
	.4byte	.LASF180
	.byte	0x7
	.byte	0
	.uleb128 0x4
	.4byte	.LASF181
	.byte	0x9
	.byte	0x78
	.byte	0x3
	.4byte	0xc7c
	.uleb128 0x13
	.byte	0x8
	.byte	0xa
	.byte	0x3c
	.byte	0x9
	.4byte	0xceb
	.uleb128 0x15
	.4byte	.LASF182
	.byte	0xa
	.byte	0x3e
	.byte	0x15
	.4byte	0xceb
	.byte	0
	.uleb128 0x15
	.4byte	.LASF183
	.byte	0xa
	.byte	0x3f
	.byte	0x15
	.4byte	0x75
	.byte	0x4
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0x4d8
	.uleb128 0x4
	.4byte	.LASF184
	.byte	0xa
	.byte	0x40
	.byte	0x3
	.4byte	0xcc7
	.uleb128 0x1c
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0xa
	.byte	0x56
	.byte	0x6
	.4byte	0xd2a
	.uleb128 0x12
	.4byte	.LASF185
	.byte	0
	.uleb128 0x12
	.4byte	.LASF186
	.byte	0x1
	.uleb128 0x12
	.4byte	.LASF187
	.byte	0x2
	.uleb128 0x12
	.4byte	.LASF188
	.byte	0x3
	.uleb128 0x12
	.4byte	.LASF189
	.byte	0x4
	.byte	0
	.uleb128 0x1c
	.byte	0x7
	.byte	0x1
	.4byte	0x41
	.byte	0xa
	.byte	0x7a
	.byte	0x1
	.4byte	0xd4b
	.uleb128 0x12
	.4byte	.LASF190
	.byte	0
	.uleb128 0x12
	.4byte	.LASF191
	.byte	0x1
	.uleb128 0x12
	.4byte	.LASF192
	.byte	0x2
	.byte	0
	.uleb128 0x4
	.4byte	.LASF193
	.byte	0xa
	.byte	0x7e
	.byte	0x3
	.4byte	0xd2a
	.uleb128 0x13
	.byte	0xc
	.byte	0xa
	.byte	0x81
	.byte	0x9
	.4byte	0xd88
	.uleb128 0x15
	.4byte	.LASF194
	.byte	0xa
	.byte	0x83
	.byte	0x1a
	.4byte	0xd4b
	.byte	0
	.uleb128 0x15
	.4byte	.LASF195
	.byte	0xa
	.byte	0x84
	.byte	0x1a
	.4byte	0x4f
	.byte	0x4
	.uleb128 0x15
	.4byte	.LASF196
	.byte	0xa
	.byte	0x85
	.byte	0x1a
	.4byte	0x4f
	.byte	0x8
	.byte	0
	.uleb128 0x4
	.4byte	.LASF197
	.byte	0xa
	.byte	0x86
	.byte	0x3
	.4byte	0xd57
	.uleb128 0x13
	.byte	0x18
	.byte	0xa
	.byte	0x99
	.byte	0x9
	.4byte	0xe2d
	.uleb128 0x15
	.4byte	.LASF198
	.byte	0xa
	.byte	0x9b
	.byte	0x1a
	.4byte	0x99
	.byte	0
	.uleb128 0x15
	.4byte	.LASF199
	.byte	0xa
	.byte	0x9e
	.byte	0x1a
	.4byte	0x99
	.byte	0x4
	.uleb128 0x15
	.4byte	.LASF200
	.byte	0xa
	.byte	0xa1
	.byte	0x1a
	.4byte	0x99
	.byte	0x8
	.uleb128 0x15
	.4byte	.LASF201
	.byte	0xa
	.byte	0xa2
	.byte	0x1a
	.4byte	0x99
	.byte	0xc
	.uleb128 0x15
	.4byte	.LASF202
	.byte	0xa
	.byte	0xa3
	.byte	0x1a
	.4byte	0xc1c
	.byte	0x10
	.uleb128 0x15
	.4byte	.LASF203
	.byte	0xa
	.byte	0xa4
	.byte	0x1a
	.4byte	0xc43
	.byte	0x11
	.uleb128 0x15
	.4byte	.LASF204
	.byte	0xa
	.byte	0xa5
	.byte	0x1a
	.4byte	0xc70
	.byte	0x12
	.uleb128 0x15
	.4byte	.LASF205
	.byte	0xa
	.byte	0xa6
	.byte	0x1a
	.4byte	0xcbb
	.byte	0x13
	.uleb128 0x14
	.ascii	"def\000"
	.byte	0xa
	.byte	0xa7
	.byte	0x1a
	.4byte	0x75
	.byte	0x14
	.uleb128 0x14
	.ascii	"orc\000"
	.byte	0xa
	.byte	0xa8
	.byte	0x1a
	.4byte	0x75
	.byte	0x15
	.uleb128 0x15
	.4byte	.LASF206
	.byte	0xa
	.byte	0xa9
	.byte	0x1a
	.4byte	0x75
	.byte	0x16
	.byte	0
	.uleb128 0x4
	.4byte	.LASF207
	.byte	0xa
	.byte	0xaa
	.byte	0x3
	.4byte	0xd94
	.uleb128 0x4
	.4byte	.LASF208
	.byte	0xb
	.byte	0x3b
	.byte	0x1d
	.4byte	0xcf1
	.uleb128 0x6
	.4byte	0xe39
	.uleb128 0x4
	.4byte	.LASF209
	.byte	0xb
	.byte	0x3d
	.byte	0x1d
	.4byte	0xe2d
	.uleb128 0x4
	.4byte	.LASF210
	.byte	0xb
	.byte	0x3f
	.byte	0x1d
	.4byte	0xd88
	.uleb128 0x1d
	.4byte	.LASF211
	.byte	0x3
	.byte	0x90
	.byte	0x11
	.4byte	0x99
	.uleb128 0x1d
	.4byte	.LASF212
	.byte	0x3
	.byte	0x92
	.byte	0x10
	.4byte	0x8d
	.uleb128 0x1d
	.4byte	.LASF213
	.byte	0xc
	.byte	0x5
	.byte	0xf
	.4byte	0x62
	.uleb128 0x1e
	.4byte	.LASF335
	.byte	0x8
	.byte	0xd
	.byte	0xa
	.byte	0x10
	.4byte	0xeae
	.uleb128 0x15
	.4byte	.LASF214
	.byte	0xd
	.byte	0xb
	.byte	0xf
	.4byte	0x825
	.byte	0
	.uleb128 0x15
	.4byte	.LASF215
	.byte	0xd
	.byte	0xc
	.byte	0xf
	.4byte	0x99
	.byte	0x4
	.byte	0
	.uleb128 0x4
	.4byte	.LASF216
	.byte	0xd
	.byte	0xe
	.byte	0x3
	.4byte	0xe86
	.uleb128 0x1f
	.4byte	0xe7a
	.byte	0x4
	.byte	0xf
	.byte	0x8
	.uleb128 0x5
	.byte	0x3
	.4byte	SWITCH2SPI
	.uleb128 0x20
	.4byte	.LASF217
	.byte	0x4
	.byte	0x13
	.byte	0x1d
	.4byte	0xe45
	.uleb128 0x5
	.byte	0x3
	.4byte	spis
	.uleb128 0x20
	.4byte	.LASF218
	.byte	0x4
	.byte	0x16
	.byte	0x17
	.4byte	0xaf
	.uleb128 0x5
	.byte	0x3
	.4byte	m_rx_length
	.uleb128 0x20
	.4byte	.LASF219
	.byte	0x4
	.byte	0x17
	.byte	0x17
	.4byte	0xaf
	.uleb128 0x5
	.byte	0x3
	.4byte	m_tx_max__length
	.uleb128 0x20
	.4byte	.LASF220
	.byte	0x4
	.byte	0x18
	.byte	0x11
	.4byte	0x99
	.uleb128 0x5
	.byte	0x3
	.4byte	m_tx_length
	.uleb128 0x20
	.4byte	.LASF221
	.byte	0x4
	.byte	0x19
	.byte	0x15
	.4byte	0x825
	.uleb128 0x5
	.byte	0x3
	.4byte	m_tx_buf
	.uleb128 0x20
	.4byte	.LASF222
	.byte	0x4
	.byte	0x1a
	.byte	0x15
	.4byte	0x825
	.uleb128 0x5
	.byte	0x3
	.4byte	m_rx_buf
	.uleb128 0x20
	.4byte	.LASF223
	.byte	0x4
	.byte	0x1c
	.byte	0x16
	.4byte	0xf4d
	.uleb128 0x5
	.byte	0x3
	.4byte	spis_xfer_done
	.uleb128 0x3
	.byte	0x1
	.byte	0x2
	.4byte	.LASF224
	.uleb128 0x5
	.4byte	0xf46
	.uleb128 0x21
	.4byte	.LASF228
	.byte	0x4
	.byte	0x35
	.byte	0x6
	.4byte	.LFB288
	.4byte	.LFE288-.LFB288
	.uleb128 0x1
	.byte	0x9c
	.4byte	0xfd8
	.uleb128 0x20
	.4byte	.LASF225
	.byte	0x4
	.byte	0x42
	.byte	0xf
	.4byte	0xeae
	.uleb128 0x2
	.byte	0x91
	.sleb128 -36
	.uleb128 0x20
	.4byte	.LASF226
	.byte	0x4
	.byte	0x52
	.byte	0x1b
	.4byte	0xe4a
	.uleb128 0x2
	.byte	0x91
	.sleb128 -60
	.uleb128 0x22
	.4byte	.LBB3
	.4byte	.LBE3-.LBB3
	.4byte	0xfa1
	.uleb128 0x23
	.ascii	"i\000"
	.byte	0x4
	.byte	0x4c
	.byte	0x14
	.4byte	0x99
	.uleb128 0x2
	.byte	0x91
	.sleb128 -20
	.byte	0
	.uleb128 0x22
	.4byte	.LBB4
	.4byte	.LBE4-.LBB4
	.4byte	0xfbe
	.uleb128 0x20
	.4byte	.LASF227
	.byte	0x4
	.byte	0x59
	.byte	0x5
	.4byte	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -24
	.byte	0
	.uleb128 0x24
	.4byte	.LBB5
	.4byte	.LBE5-.LBB5
	.uleb128 0x20
	.4byte	.LASF227
	.byte	0x4
	.byte	0x61
	.byte	0x9
	.4byte	0xaf
	.uleb128 0x2
	.byte	0x91
	.sleb128 -28
	.byte	0
	.byte	0
	.uleb128 0x21
	.4byte	.LASF229
	.byte	0x4
	.byte	0x23
	.byte	0x6
	.4byte	.LFB287
	.4byte	.LFE287-.LFB287
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1035
	.uleb128 0x25
	.4byte	.LASF233
	.byte	0x4
	.byte	0x23
	.byte	0x2e
	.4byte	0xe56
	.uleb128 0x2
	.byte	0x91
	.sleb128 -28
	.uleb128 0x24
	.4byte	.LBB2
	.4byte	.LBE2-.LBB2
	.uleb128 0x20
	.4byte	.LASF230
	.byte	0x4
	.byte	0x2a
	.byte	0x11
	.4byte	0x75
	.uleb128 0x2
	.byte	0x91
	.sleb128 -9
	.uleb128 0x20
	.4byte	.LASF231
	.byte	0x4
	.byte	0x2b
	.byte	0x11
	.4byte	0x75
	.uleb128 0x2
	.byte	0x91
	.sleb128 -10
	.uleb128 0x20
	.4byte	.LASF232
	.byte	0x4
	.byte	0x2c
	.byte	0x12
	.4byte	0x99
	.uleb128 0x2
	.byte	0x91
	.sleb128 -16
	.byte	0
	.byte	0
	.uleb128 0x26
	.4byte	.LASF239
	.byte	0x3
	.byte	0xc6
	.byte	0x18
	.4byte	0x99
	.4byte	.LFB286
	.4byte	.LFE286-.LFB286
	.uleb128 0x1
	.byte	0x9c
	.uleb128 0x27
	.4byte	.LASF236
	.byte	0x2
	.2byte	0x42f
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB211
	.4byte	.LFE211-.LFB211
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1085
	.uleb128 0x28
	.4byte	.LASF234
	.byte	0x2
	.2byte	0x42f
	.byte	0x1
	.4byte	0x1085
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF235
	.byte	0x2
	.2byte	0x42f
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xa5
	.uleb128 0x27
	.4byte	.LASF237
	.byte	0x2
	.2byte	0x41a
	.byte	0x2
	.4byte	0x99
	.4byte	.LFB210
	.4byte	.LFE210-.LFB210
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x10b6
	.uleb128 0x28
	.4byte	.LASF238
	.byte	0x2
	.2byte	0x41a
	.byte	0x2
	.4byte	0x10b6
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xa6a
	.uleb128 0x29
	.4byte	.LASF240
	.byte	0x2
	.2byte	0x3f5
	.byte	0x2
	.4byte	0x99
	.4byte	.LFB209
	.4byte	.LFE209-.LFB209
	.uleb128 0x1
	.byte	0x9c
	.uleb128 0x27
	.4byte	.LASF241
	.byte	0x2
	.2byte	0x3e8
	.byte	0x2
	.4byte	0x99
	.4byte	.LFB208
	.4byte	.LFE208-.LFB208
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x10fe
	.uleb128 0x28
	.4byte	.LASF242
	.byte	0x2
	.2byte	0x3e8
	.byte	0x2
	.4byte	0xb00
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF243
	.byte	0x2
	.2byte	0x3d0
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB207
	.4byte	.LFE207-.LFB207
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1129
	.uleb128 0x28
	.4byte	.LASF244
	.byte	0x2
	.2byte	0x3d0
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF245
	.byte	0x2
	.2byte	0x3b0
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB206
	.4byte	.LFE206-.LFB206
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1172
	.uleb128 0x28
	.4byte	.LASF246
	.byte	0x2
	.2byte	0x3b0
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF247
	.byte	0x2
	.2byte	0x3b0
	.byte	0x1
	.4byte	0x1172
	.uleb128 0x1
	.byte	0x51
	.uleb128 0x28
	.4byte	.LASF248
	.byte	0x2
	.2byte	0x3b0
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x52
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xaf
	.uleb128 0x27
	.4byte	.LASF249
	.byte	0x2
	.2byte	0x38b
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB205
	.4byte	.LFE205-.LFB205
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x11a3
	.uleb128 0x28
	.4byte	.LASF250
	.byte	0x2
	.2byte	0x38b
	.byte	0x1
	.4byte	0x11a3
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0x8d
	.uleb128 0x27
	.4byte	.LASF251
	.byte	0x2
	.2byte	0x380
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB204
	.4byte	.LFE204-.LFB204
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x11d4
	.uleb128 0x28
	.4byte	.LASF252
	.byte	0x2
	.2byte	0x380
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF253
	.byte	0x2
	.2byte	0x375
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB203
	.4byte	.LFE203-.LFB203
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x120e
	.uleb128 0x28
	.4byte	.LASF254
	.byte	0x2
	.2byte	0x375
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF255
	.byte	0x2
	.2byte	0x375
	.byte	0x1
	.4byte	0x120e
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xbe8
	.uleb128 0x27
	.4byte	.LASF256
	.byte	0x2
	.2byte	0x364
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB202
	.4byte	.LFE202-.LFB202
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x123f
	.uleb128 0x28
	.4byte	.LASF257
	.byte	0x2
	.2byte	0x364
	.byte	0x1
	.4byte	0x123f
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0xb94
	.uleb128 0x27
	.4byte	.LASF258
	.byte	0x2
	.2byte	0x354
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB201
	.4byte	.LFE201-.LFB201
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x127f
	.uleb128 0x28
	.4byte	.LASF259
	.byte	0x2
	.2byte	0x354
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF260
	.byte	0x2
	.2byte	0x354
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF261
	.byte	0x2
	.2byte	0x335
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB200
	.4byte	.LFE200-.LFB200
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x12b9
	.uleb128 0x28
	.4byte	.LASF262
	.byte	0x2
	.2byte	0x335
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF263
	.byte	0x2
	.2byte	0x335
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF264
	.byte	0x2
	.2byte	0x32b
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB199
	.4byte	.LFE199-.LFB199
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x12f3
	.uleb128 0x28
	.4byte	.LASF262
	.byte	0x2
	.2byte	0x32b
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF265
	.byte	0x2
	.2byte	0x32b
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF266
	.byte	0x2
	.2byte	0x321
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB198
	.4byte	.LFE198-.LFB198
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x131e
	.uleb128 0x28
	.4byte	.LASF262
	.byte	0x2
	.2byte	0x321
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF267
	.byte	0x2
	.2byte	0x318
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB197
	.4byte	.LFE197-.LFB197
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1349
	.uleb128 0x28
	.4byte	.LASF262
	.byte	0x2
	.2byte	0x318
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF268
	.byte	0x2
	.2byte	0x30f
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB196
	.4byte	.LFE196-.LFB196
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1392
	.uleb128 0x28
	.4byte	.LASF269
	.byte	0x2
	.2byte	0x30f
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF270
	.byte	0x2
	.2byte	0x30f
	.byte	0x1
	.4byte	0x1392
	.uleb128 0x1
	.byte	0x51
	.uleb128 0x28
	.4byte	.LASF271
	.byte	0x2
	.2byte	0x30f
	.byte	0x1
	.4byte	0x1392
	.uleb128 0x1
	.byte	0x52
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0x1399
	.uleb128 0x2a
	.uleb128 0x5
	.4byte	0x1398
	.uleb128 0x27
	.4byte	.LASF272
	.byte	0x2
	.2byte	0x304
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB195
	.4byte	.LFE195-.LFB195
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x13c9
	.uleb128 0x28
	.4byte	.LASF273
	.byte	0x2
	.2byte	0x304
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF274
	.byte	0x2
	.2byte	0x2fc
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB194
	.4byte	.LFE194-.LFB194
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x13f4
	.uleb128 0x28
	.4byte	.LASF275
	.byte	0x2
	.2byte	0x2fc
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF276
	.byte	0x2
	.2byte	0x2f4
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB193
	.4byte	.LFE193-.LFB193
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x141f
	.uleb128 0x28
	.4byte	.LASF277
	.byte	0x2
	.2byte	0x2f4
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x29
	.4byte	.LASF278
	.byte	0x2
	.2byte	0x2ec
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB192
	.4byte	.LFE192-.LFB192
	.uleb128 0x1
	.byte	0x9c
	.uleb128 0x27
	.4byte	.LASF279
	.byte	0x2
	.2byte	0x2d0
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB191
	.4byte	.LFE191-.LFB191
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1461
	.uleb128 0x28
	.4byte	.LASF280
	.byte	0x2
	.2byte	0x2d0
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x29
	.4byte	.LASF281
	.byte	0x2
	.2byte	0x2c5
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB190
	.4byte	.LFE190-.LFB190
	.uleb128 0x1
	.byte	0x9c
	.uleb128 0x29
	.4byte	.LASF282
	.byte	0x2
	.2byte	0x2ba
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB189
	.4byte	.LFE189-.LFB189
	.uleb128 0x1
	.byte	0x9c
	.uleb128 0x27
	.4byte	.LASF283
	.byte	0x2
	.2byte	0x2ae
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB188
	.4byte	.LFE188-.LFB188
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x14ba
	.uleb128 0x28
	.4byte	.LASF284
	.byte	0x2
	.2byte	0x2ae
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF285
	.byte	0x2
	.2byte	0x2a3
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB187
	.4byte	.LFE187-.LFB187
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x14e5
	.uleb128 0x28
	.4byte	.LASF284
	.byte	0x2
	.2byte	0x2a3
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF286
	.byte	0x2
	.2byte	0x29a
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB186
	.4byte	.LFE186-.LFB186
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x151f
	.uleb128 0x28
	.4byte	.LASF287
	.byte	0x2
	.2byte	0x29a
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF288
	.byte	0x2
	.2byte	0x29a
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF289
	.byte	0x2
	.2byte	0x291
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB185
	.4byte	.LFE185-.LFB185
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1559
	.uleb128 0x28
	.4byte	.LASF287
	.byte	0x2
	.2byte	0x291
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF290
	.byte	0x2
	.2byte	0x291
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF291
	.byte	0x2
	.2byte	0x288
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB184
	.4byte	.LFE184-.LFB184
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1593
	.uleb128 0x28
	.4byte	.LASF287
	.byte	0x2
	.2byte	0x288
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF290
	.byte	0x2
	.2byte	0x288
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF292
	.byte	0x2
	.2byte	0x27f
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB183
	.4byte	.LFE183-.LFB183
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x15cd
	.uleb128 0x28
	.4byte	.LASF293
	.byte	0x2
	.2byte	0x27f
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF294
	.byte	0x2
	.2byte	0x27f
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF295
	.byte	0x2
	.2byte	0x276
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB182
	.4byte	.LFE182-.LFB182
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1607
	.uleb128 0x28
	.4byte	.LASF293
	.byte	0x2
	.2byte	0x276
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF296
	.byte	0x2
	.2byte	0x276
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF297
	.byte	0x2
	.2byte	0x26d
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB181
	.4byte	.LFE181-.LFB181
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1641
	.uleb128 0x28
	.4byte	.LASF293
	.byte	0x2
	.2byte	0x26d
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF298
	.byte	0x2
	.2byte	0x26d
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF299
	.byte	0x2
	.2byte	0x264
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB180
	.4byte	.LFE180-.LFB180
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x166c
	.uleb128 0x28
	.4byte	.LASF300
	.byte	0x2
	.2byte	0x264
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF301
	.byte	0x2
	.2byte	0x257
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB179
	.4byte	.LFE179-.LFB179
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1697
	.uleb128 0x28
	.4byte	.LASF300
	.byte	0x2
	.2byte	0x257
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF302
	.byte	0x2
	.2byte	0x24a
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB178
	.4byte	.LFE178-.LFB178
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x16c2
	.uleb128 0x28
	.4byte	.LASF303
	.byte	0x2
	.2byte	0x24a
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF304
	.byte	0x2
	.2byte	0x240
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB177
	.4byte	.LFE177-.LFB177
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x16ed
	.uleb128 0x28
	.4byte	.LASF305
	.byte	0x2
	.2byte	0x240
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF306
	.byte	0x2
	.2byte	0x233
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB176
	.4byte	.LFE176-.LFB176
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1718
	.uleb128 0x28
	.4byte	.LASF307
	.byte	0x2
	.2byte	0x233
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF308
	.byte	0x2
	.2byte	0x226
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB175
	.4byte	.LFE175-.LFB175
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1743
	.uleb128 0x28
	.4byte	.LASF309
	.byte	0x2
	.2byte	0x226
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF310
	.byte	0x2
	.2byte	0x219
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB174
	.4byte	.LFE174-.LFB174
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x176e
	.uleb128 0x28
	.4byte	.LASF311
	.byte	0x2
	.2byte	0x219
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x29
	.4byte	.LASF312
	.byte	0x2
	.2byte	0x20e
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB173
	.4byte	.LFE173-.LFB173
	.uleb128 0x1
	.byte	0x9c
	.uleb128 0x27
	.4byte	.LASF313
	.byte	0x2
	.2byte	0x208
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB172
	.4byte	.LFE172-.LFB172
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x17b0
	.uleb128 0x28
	.4byte	.LASF314
	.byte	0x2
	.2byte	0x208
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF315
	.byte	0x2
	.2byte	0x1ff
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB171
	.4byte	.LFE171-.LFB171
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x17db
	.uleb128 0x28
	.4byte	.LASF316
	.byte	0x2
	.2byte	0x1ff
	.byte	0x1
	.4byte	0x99
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF317
	.byte	0x2
	.2byte	0x1f7
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB170
	.4byte	.LFE170-.LFB170
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1806
	.uleb128 0x28
	.4byte	.LASF318
	.byte	0x2
	.2byte	0x1f7
	.byte	0x1
	.4byte	0x6a0
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF319
	.byte	0x2
	.2byte	0x1ef
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB169
	.4byte	.LFE169-.LFB169
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1840
	.uleb128 0x28
	.4byte	.LASF320
	.byte	0x2
	.2byte	0x1ef
	.byte	0x1
	.4byte	0x825
	.uleb128 0x1
	.byte	0x50
	.uleb128 0x28
	.4byte	.LASF321
	.byte	0x2
	.2byte	0x1ef
	.byte	0x1
	.4byte	0x75
	.uleb128 0x1
	.byte	0x51
	.byte	0
	.uleb128 0x27
	.4byte	.LASF322
	.byte	0x2
	.2byte	0x1e5
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB168
	.4byte	.LFE168-.LFB168
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x186b
	.uleb128 0x28
	.4byte	.LASF323
	.byte	0x2
	.2byte	0x1e5
	.byte	0x1
	.4byte	0x825
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF324
	.byte	0x2
	.2byte	0x1dd
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB167
	.4byte	.LFE167-.LFB167
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1896
	.uleb128 0x28
	.4byte	.LASF325
	.byte	0x2
	.2byte	0x1dd
	.byte	0x1
	.4byte	0x825
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF326
	.byte	0x2
	.2byte	0x1d5
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB166
	.4byte	.LFE166-.LFB166
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x18c1
	.uleb128 0x28
	.4byte	.LASF327
	.byte	0x2
	.2byte	0x1d5
	.byte	0x1
	.4byte	0x18c1
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0x964
	.uleb128 0x27
	.4byte	.LASF328
	.byte	0x2
	.2byte	0x1cd
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB165
	.4byte	.LFE165-.LFB165
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x18f2
	.uleb128 0x28
	.4byte	.LASF327
	.byte	0x2
	.2byte	0x1cd
	.byte	0x1
	.4byte	0x18c1
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF329
	.byte	0x2
	.2byte	0x1c4
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB164
	.4byte	.LFE164-.LFB164
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x191d
	.uleb128 0x28
	.4byte	.LASF327
	.byte	0x2
	.2byte	0x1c4
	.byte	0x1
	.4byte	0x18c1
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x27
	.4byte	.LASF330
	.byte	0x1
	.2byte	0x101
	.byte	0x1
	.4byte	0x99
	.4byte	.LFB138
	.4byte	.LFE138-.LFB138
	.uleb128 0x1
	.byte	0x9c
	.4byte	0x1948
	.uleb128 0x28
	.4byte	.LASF331
	.byte	0x1
	.2byte	0x101
	.byte	0x1
	.4byte	0x1948
	.uleb128 0x1
	.byte	0x50
	.byte	0
	.uleb128 0x10
	.byte	0x4
	.4byte	0x819
	.byte	0
	.section	.debug_abbrev,"",%progbits
.Ldebug_abbrev0:
	.uleb128 0x1
	.uleb128 0x11
	.byte	0x1
	.uleb128 0x25
	.uleb128 0xe
	.uleb128 0x13
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x1b
	.uleb128 0xe
	.uleb128 0x2134
	.uleb128 0x19
	.uleb128 0x55
	.uleb128 0x17
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x10
	.uleb128 0x17
	.byte	0
	.byte	0
	.uleb128 0x2
	.uleb128 0x24
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0x8
	.byte	0
	.byte	0
	.uleb128 0x3
	.uleb128 0x24
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0xe
	.byte	0
	.byte	0
	.uleb128 0x4
	.uleb128 0x16
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x5
	.uleb128 0x35
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x6
	.uleb128 0x26
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x7
	.uleb128 0x1
	.byte	0x1
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x8
	.uleb128 0x21
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2f
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0x9
	.uleb128 0x13
	.byte	0x1
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xa
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0xb
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0xc
	.uleb128 0x16
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xd
	.uleb128 0x13
	.byte	0x1
	.uleb128 0xb
	.uleb128 0x5
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xe
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0x5
	.byte	0
	.byte	0
	.uleb128 0xf
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0x5
	.byte	0
	.byte	0
	.uleb128 0x10
	.uleb128 0xf
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x11
	.uleb128 0x4
	.byte	0x1
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x12
	.uleb128 0x28
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x1c
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0x13
	.uleb128 0x13
	.byte	0x1
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x14
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0x15
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xb
	.byte	0
	.byte	0
	.uleb128 0x16
	.uleb128 0x17
	.byte	0x1
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x17
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x18
	.uleb128 0x17
	.byte	0x1
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x19
	.uleb128 0xd
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x1a
	.uleb128 0x15
	.byte	0x1
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x1b
	.uleb128 0x5
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x1c
	.uleb128 0x4
	.byte	0x1
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x1d
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3c
	.uleb128 0x19
	.byte	0
	.byte	0
	.uleb128 0x1e
	.uleb128 0x13
	.byte	0x1
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x1f
	.uleb128 0x34
	.byte	0
	.uleb128 0x47
	.uleb128 0x13
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x20
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x21
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x6
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x2116
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x22
	.uleb128 0xb
	.byte	0x1
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x6
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x23
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x24
	.uleb128 0xb
	.byte	0x1
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x6
	.byte	0
	.byte	0
	.uleb128 0x25
	.uleb128 0x5
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x26
	.uleb128 0x2e
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x6
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x2117
	.uleb128 0x19
	.byte	0
	.byte	0
	.uleb128 0x27
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x6
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x2117
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x28
	.uleb128 0x5
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x29
	.uleb128 0x2e
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x6
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x2117
	.uleb128 0x19
	.byte	0
	.byte	0
	.uleb128 0x2a
	.uleb128 0x26
	.byte	0
	.byte	0
	.byte	0
	.byte	0
	.section	.debug_pubnames,"",%progbits
	.4byte	0xdae
	.2byte	0x2
	.4byte	.Ldebug_info0
	.4byte	0x194f
	.4byte	0x6b8
	.ascii	"SD_MBR_COMMAND\000"
	.4byte	0x83d
	.ascii	"SD_PPI_CHANNEL_ENABLE_GET\000"
	.4byte	0x843
	.ascii	"SD_PPI_CHANNEL_ENABLE_SET\000"
	.4byte	0x849
	.ascii	"SD_PPI_CHANNEL_ENABLE_CLR\000"
	.4byte	0x84f
	.ascii	"SD_PPI_CHANNEL_ASSIGN\000"
	.4byte	0x855
	.ascii	"SD_PPI_GROUP_TASK_ENABLE\000"
	.4byte	0x85b
	.ascii	"SD_PPI_GROUP_TASK_DISABLE\000"
	.4byte	0x861
	.ascii	"SD_PPI_GROUP_ASSIGN\000"
	.4byte	0x867
	.ascii	"SD_PPI_GROUP_GET\000"
	.4byte	0x86d
	.ascii	"SD_FLASH_PAGE_ERASE\000"
	.4byte	0x873
	.ascii	"SD_FLASH_WRITE\000"
	.4byte	0x879
	.ascii	"SD_PROTECTED_REGISTER_WRITE\000"
	.4byte	0x87f
	.ascii	"SD_MUTEX_NEW\000"
	.4byte	0x885
	.ascii	"SD_MUTEX_ACQUIRE\000"
	.4byte	0x88b
	.ascii	"SD_MUTEX_RELEASE\000"
	.4byte	0x891
	.ascii	"SD_RAND_APPLICATION_POOL_CAPACITY_GET\000"
	.4byte	0x897
	.ascii	"SD_RAND_APPLICATION_BYTES_AVAILABLE_GET\000"
	.4byte	0x89d
	.ascii	"SD_RAND_APPLICATION_VECTOR_GET\000"
	.4byte	0x8a3
	.ascii	"SD_POWER_MODE_SET\000"
	.4byte	0x8a9
	.ascii	"SD_POWER_SYSTEM_OFF\000"
	.4byte	0x8af
	.ascii	"SD_POWER_RESET_REASON_GET\000"
	.4byte	0x8b5
	.ascii	"SD_POWER_RESET_REASON_CLR\000"
	.4byte	0x8bb
	.ascii	"SD_POWER_POF_ENABLE\000"
	.4byte	0x8c1
	.ascii	"SD_POWER_POF_THRESHOLD_SET\000"
	.4byte	0x8c7
	.ascii	"SD_POWER_POF_THRESHOLDVDDH_SET\000"
	.4byte	0x8cd
	.ascii	"SD_POWER_RAM_POWER_SET\000"
	.4byte	0x8d3
	.ascii	"SD_POWER_RAM_POWER_CLR\000"
	.4byte	0x8d9
	.ascii	"SD_POWER_RAM_POWER_GET\000"
	.4byte	0x8df
	.ascii	"SD_POWER_GPREGRET_SET\000"
	.4byte	0x8e5
	.ascii	"SD_POWER_GPREGRET_CLR\000"
	.4byte	0x8eb
	.ascii	"SD_POWER_GPREGRET_GET\000"
	.4byte	0x8f1
	.ascii	"SD_POWER_DCDC_MODE_SET\000"
	.4byte	0x8f7
	.ascii	"SD_POWER_DCDC0_MODE_SET\000"
	.4byte	0x8fd
	.ascii	"SD_APP_EVT_WAIT\000"
	.4byte	0x903
	.ascii	"SD_CLOCK_HFCLK_REQUEST\000"
	.4byte	0x909
	.ascii	"SD_CLOCK_HFCLK_RELEASE\000"
	.4byte	0x90f
	.ascii	"SD_CLOCK_HFCLK_IS_RUNNING\000"
	.4byte	0x915
	.ascii	"SD_RADIO_NOTIFICATION_CFG_SET\000"
	.4byte	0x91b
	.ascii	"SD_ECB_BLOCK_ENCRYPT\000"
	.4byte	0x921
	.ascii	"SD_ECB_BLOCKS_ENCRYPT\000"
	.4byte	0x927
	.ascii	"SD_RADIO_SESSION_OPEN\000"
	.4byte	0x92d
	.ascii	"SD_RADIO_SESSION_CLOSE\000"
	.4byte	0x933
	.ascii	"SD_RADIO_REQUEST\000"
	.4byte	0x939
	.ascii	"SD_EVT_GET\000"
	.4byte	0x93f
	.ascii	"SD_TEMP_GET\000"
	.4byte	0x945
	.ascii	"SD_POWER_USBPWRRDY_ENABLE\000"
	.4byte	0x94b
	.ascii	"SD_POWER_USBDETECTED_ENABLE\000"
	.4byte	0x951
	.ascii	"SD_POWER_USBREMOVED_ENABLE\000"
	.4byte	0x957
	.ascii	"SD_POWER_USBREGSTATUS_GET\000"
	.4byte	0x95d
	.ascii	"SVC_SOC_LAST\000"
	.4byte	0xc03
	.ascii	"NRF_SPIS_MODE_0\000"
	.4byte	0xc09
	.ascii	"NRF_SPIS_MODE_1\000"
	.4byte	0xc0f
	.ascii	"NRF_SPIS_MODE_2\000"
	.4byte	0xc15
	.ascii	"NRF_SPIS_MODE_3\000"
	.4byte	0xc36
	.ascii	"NRF_SPIS_BIT_ORDER_MSB_FIRST\000"
	.4byte	0xc3c
	.ascii	"NRF_SPIS_BIT_ORDER_LSB_FIRST\000"
	.4byte	0xc5d
	.ascii	"NRF_GPIO_PIN_NOPULL\000"
	.4byte	0xc63
	.ascii	"NRF_GPIO_PIN_PULLDOWN\000"
	.4byte	0xc69
	.ascii	"NRF_GPIO_PIN_PULLUP\000"
	.4byte	0xc8a
	.ascii	"NRF_GPIO_PIN_S0S1\000"
	.4byte	0xc90
	.ascii	"NRF_GPIO_PIN_H0S1\000"
	.4byte	0xc96
	.ascii	"NRF_GPIO_PIN_S0H1\000"
	.4byte	0xc9c
	.ascii	"NRF_GPIO_PIN_H0H1\000"
	.4byte	0xca2
	.ascii	"NRF_GPIO_PIN_D0S1\000"
	.4byte	0xca8
	.ascii	"NRF_GPIO_PIN_D0H1\000"
	.4byte	0xcae
	.ascii	"NRF_GPIO_PIN_S0D1\000"
	.4byte	0xcb4
	.ascii	"NRF_GPIO_PIN_H0D1\000"
	.4byte	0xd0b
	.ascii	"NRFX_SPIS0_INST_IDX\000"
	.4byte	0xd11
	.ascii	"NRFX_SPIS1_INST_IDX\000"
	.4byte	0xd17
	.ascii	"NRFX_SPIS2_INST_IDX\000"
	.4byte	0xd1d
	.ascii	"NRFX_SPIS3_INST_IDX\000"
	.4byte	0xd23
	.ascii	"NRFX_SPIS_ENABLED_COUNT\000"
	.4byte	0xd38
	.ascii	"NRFX_SPIS_BUFFERS_SET_DONE\000"
	.4byte	0xd3e
	.ascii	"NRFX_SPIS_XFER_DONE\000"
	.4byte	0xd44
	.ascii	"NRFX_SPIS_EVT_TYPE_MAX\000"
	.4byte	0xeba
	.ascii	"SWITCH2SPI\000"
	.4byte	0xec8
	.ascii	"spis\000"
	.4byte	0xeda
	.ascii	"m_rx_length\000"
	.4byte	0xeec
	.ascii	"m_tx_max__length\000"
	.4byte	0xefe
	.ascii	"m_tx_length\000"
	.4byte	0xf10
	.ascii	"m_tx_buf\000"
	.4byte	0xf22
	.ascii	"m_rx_buf\000"
	.4byte	0xf34
	.ascii	"spis_xfer_done\000"
	.4byte	0xf10
	.ascii	"m_tx_buf\000"
	.4byte	0xf22
	.ascii	"m_rx_buf\000"
	.4byte	0xf34
	.ascii	"spis_xfer_done\000"
	.4byte	0xf52
	.ascii	"spis_start\000"
	.4byte	0xfd8
	.ascii	"spis_event_handler\000"
	.4byte	0x1035
	.ascii	"log_timestamp_get\000"
	.4byte	0x104b
	.ascii	"sd_protected_register_write\000"
	.4byte	0x108b
	.ascii	"sd_radio_request\000"
	.4byte	0x10bc
	.ascii	"sd_radio_session_close\000"
	.4byte	0x10d3
	.ascii	"sd_radio_session_open\000"
	.4byte	0x10fe
	.ascii	"sd_flash_page_erase\000"
	.4byte	0x1129
	.ascii	"sd_flash_write\000"
	.4byte	0x1178
	.ascii	"sd_temp_get\000"
	.4byte	0x11a9
	.ascii	"sd_evt_get\000"
	.4byte	0x11d4
	.ascii	"sd_ecb_blocks_encrypt\000"
	.4byte	0x1214
	.ascii	"sd_ecb_block_encrypt\000"
	.4byte	0x1245
	.ascii	"sd_radio_notification_cfg_set\000"
	.4byte	0x127f
	.ascii	"sd_ppi_group_get\000"
	.4byte	0x12b9
	.ascii	"sd_ppi_group_assign\000"
	.4byte	0x12f3
	.ascii	"sd_ppi_group_task_disable\000"
	.4byte	0x131e
	.ascii	"sd_ppi_group_task_enable\000"
	.4byte	0x1349
	.ascii	"sd_ppi_channel_assign\000"
	.4byte	0x139e
	.ascii	"sd_ppi_channel_enable_clr\000"
	.4byte	0x13c9
	.ascii	"sd_ppi_channel_enable_set\000"
	.4byte	0x13f4
	.ascii	"sd_ppi_channel_enable_get\000"
	.4byte	0x141f
	.ascii	"sd_app_evt_wait\000"
	.4byte	0x1436
	.ascii	"sd_clock_hfclk_is_running\000"
	.4byte	0x1461
	.ascii	"sd_clock_hfclk_release\000"
	.4byte	0x1478
	.ascii	"sd_clock_hfclk_request\000"
	.4byte	0x148f
	.ascii	"sd_power_dcdc0_mode_set\000"
	.4byte	0x14ba
	.ascii	"sd_power_dcdc_mode_set\000"
	.4byte	0x14e5
	.ascii	"sd_power_gpregret_get\000"
	.4byte	0x151f
	.ascii	"sd_power_gpregret_clr\000"
	.4byte	0x1559
	.ascii	"sd_power_gpregret_set\000"
	.4byte	0x1593
	.ascii	"sd_power_ram_power_get\000"
	.4byte	0x15cd
	.ascii	"sd_power_ram_power_clr\000"
	.4byte	0x1607
	.ascii	"sd_power_ram_power_set\000"
	.4byte	0x1641
	.ascii	"sd_power_pof_thresholdvddh_set\000"
	.4byte	0x166c
	.ascii	"sd_power_pof_threshold_set\000"
	.4byte	0x1697
	.ascii	"sd_power_usbregstatus_get\000"
	.4byte	0x16c2
	.ascii	"sd_power_usbremoved_enable\000"
	.4byte	0x16ed
	.ascii	"sd_power_usbdetected_enable\000"
	.4byte	0x1718
	.ascii	"sd_power_usbpwrrdy_enable\000"
	.4byte	0x1743
	.ascii	"sd_power_pof_enable\000"
	.4byte	0x176e
	.ascii	"sd_power_system_off\000"
	.4byte	0x1785
	.ascii	"sd_power_mode_set\000"
	.4byte	0x17b0
	.ascii	"sd_power_reset_reason_clr\000"
	.4byte	0x17db
	.ascii	"sd_power_reset_reason_get\000"
	.4byte	0x1806
	.ascii	"sd_rand_application_vector_get\000"
	.4byte	0x1840
	.ascii	"sd_rand_application_bytes_available_get\000"
	.4byte	0x186b
	.ascii	"sd_rand_application_pool_capacity_get\000"
	.4byte	0x1896
	.ascii	"sd_mutex_release\000"
	.4byte	0x18c7
	.ascii	"sd_mutex_acquire\000"
	.4byte	0x18f2
	.ascii	"sd_mutex_new\000"
	.4byte	0x191d
	.ascii	"sd_mbr_command\000"
	.4byte	0
	.section	.debug_pubtypes,"",%progbits
	.4byte	0x484
	.2byte	0x2
	.4byte	.Ldebug_info0
	.4byte	0x194f
	.4byte	0x25
	.ascii	"int\000"
	.4byte	0x2c
	.ascii	"long int\000"
	.4byte	0x33
	.ascii	"char\000"
	.4byte	0x3a
	.ascii	"unsigned int\000"
	.4byte	0x41
	.ascii	"unsigned char\000"
	.4byte	0x48
	.ascii	"short unsigned int\000"
	.4byte	0x4f
	.ascii	"size_t\000"
	.4byte	0x5b
	.ascii	"long long int\000"
	.4byte	0x6e
	.ascii	"signed char\000"
	.4byte	0x62
	.ascii	"int8_t\000"
	.4byte	0x75
	.ascii	"uint8_t\000"
	.4byte	0x86
	.ascii	"short int\000"
	.4byte	0x8d
	.ascii	"int32_t\000"
	.4byte	0x99
	.ascii	"uint32_t\000"
	.4byte	0xb4
	.ascii	"long long unsigned int\000"
	.4byte	0xbb
	.ascii	"long double\000"
	.4byte	0x139
	.ascii	"SPIS_PSEL_Type\000"
	.4byte	0x18e
	.ascii	"SPIS_RXD_Type\000"
	.4byte	0x1e3
	.ascii	"SPIS_TXD_Type\000"
	.4byte	0x4d8
	.ascii	"NRF_SPIS_Type\000"
	.4byte	0x693
	.ascii	"NRF_RTC_Type\000"
	.4byte	0x6a6
	.ascii	"NRF_MBR_SVCS\000"
	.4byte	0x6f0
	.ascii	"sd_mbr_command_copy_sd_t\000"
	.4byte	0x72d
	.ascii	"sd_mbr_command_compare_t\000"
	.4byte	0x75d
	.ascii	"sd_mbr_command_copy_bl_t\000"
	.4byte	0x780
	.ascii	"sd_mbr_command_vector_table_base_set_t\000"
	.4byte	0x7a3
	.ascii	"sd_mbr_command_irq_forward_address_set_t\000"
	.4byte	0x819
	.ascii	"sd_mbr_command_t\000"
	.4byte	0x82b
	.ascii	"NRF_SOC_SVCS\000"
	.4byte	0x964
	.ascii	"nrf_mutex_t\000"
	.4byte	0x9b4
	.ascii	"nrf_radio_request_earliest_t\000"
	.4byte	0xa04
	.ascii	"nrf_radio_request_normal_t\000"
	.4byte	0xa5d
	.ascii	"nrf_radio_request_t\000"
	.4byte	0xaf3
	.ascii	"nrf_radio_signal_callback_return_param_t\000"
	.4byte	0xb00
	.ascii	"nrf_radio_signal_callback_t\000"
	.4byte	0xb28
	.ascii	"soc_ecb_key_t\000"
	.4byte	0xb45
	.ascii	"soc_ecb_cleartext_t\000"
	.4byte	0xb52
	.ascii	"soc_ecb_ciphertext_t\000"
	.4byte	0xb94
	.ascii	"nrf_ecb_hal_data_t\000"
	.4byte	0xbe8
	.ascii	"nrf_ecb_hal_data_block_t\000"
	.4byte	0xc1c
	.ascii	"nrf_spis_mode_t\000"
	.4byte	0xc43
	.ascii	"nrf_spis_bit_order_t\000"
	.4byte	0xc70
	.ascii	"nrf_gpio_pin_pull_t\000"
	.4byte	0xcbb
	.ascii	"nrf_gpio_pin_drive_t\000"
	.4byte	0xcf1
	.ascii	"nrfx_spis_t\000"
	.4byte	0xd4b
	.ascii	"nrfx_spis_evt_type_t\000"
	.4byte	0xd88
	.ascii	"nrfx_spis_evt_t\000"
	.4byte	0xe2d
	.ascii	"nrfx_spis_config_t\000"
	.4byte	0xe39
	.ascii	"nrf_drv_spis_t\000"
	.4byte	0xe4a
	.ascii	"nrf_drv_spis_config_t\000"
	.4byte	0xe56
	.ascii	"nrf_drv_spis_event_t\000"
	.4byte	0xe86
	.ascii	"Sen_data\000"
	.4byte	0xeae
	.ascii	"sen_data\000"
	.4byte	0xf46
	.ascii	"_Bool\000"
	.4byte	0
	.section	.debug_aranges,"",%progbits
	.4byte	0x1b4
	.2byte	0x2
	.4byte	.Ldebug_info0
	.byte	0x4
	.byte	0
	.2byte	0
	.2byte	0
	.4byte	.LFB138
	.4byte	.LFE138-.LFB138
	.4byte	.LFB164
	.4byte	.LFE164-.LFB164
	.4byte	.LFB165
	.4byte	.LFE165-.LFB165
	.4byte	.LFB166
	.4byte	.LFE166-.LFB166
	.4byte	.LFB167
	.4byte	.LFE167-.LFB167
	.4byte	.LFB168
	.4byte	.LFE168-.LFB168
	.4byte	.LFB169
	.4byte	.LFE169-.LFB169
	.4byte	.LFB170
	.4byte	.LFE170-.LFB170
	.4byte	.LFB171
	.4byte	.LFE171-.LFB171
	.4byte	.LFB172
	.4byte	.LFE172-.LFB172
	.4byte	.LFB173
	.4byte	.LFE173-.LFB173
	.4byte	.LFB174
	.4byte	.LFE174-.LFB174
	.4byte	.LFB175
	.4byte	.LFE175-.LFB175
	.4byte	.LFB176
	.4byte	.LFE176-.LFB176
	.4byte	.LFB177
	.4byte	.LFE177-.LFB177
	.4byte	.LFB178
	.4byte	.LFE178-.LFB178
	.4byte	.LFB179
	.4byte	.LFE179-.LFB179
	.4byte	.LFB180
	.4byte	.LFE180-.LFB180
	.4byte	.LFB181
	.4byte	.LFE181-.LFB181
	.4byte	.LFB182
	.4byte	.LFE182-.LFB182
	.4byte	.LFB183
	.4byte	.LFE183-.LFB183
	.4byte	.LFB184
	.4byte	.LFE184-.LFB184
	.4byte	.LFB185
	.4byte	.LFE185-.LFB185
	.4byte	.LFB186
	.4byte	.LFE186-.LFB186
	.4byte	.LFB187
	.4byte	.LFE187-.LFB187
	.4byte	.LFB188
	.4byte	.LFE188-.LFB188
	.4byte	.LFB189
	.4byte	.LFE189-.LFB189
	.4byte	.LFB190
	.4byte	.LFE190-.LFB190
	.4byte	.LFB191
	.4byte	.LFE191-.LFB191
	.4byte	.LFB192
	.4byte	.LFE192-.LFB192
	.4byte	.LFB193
	.4byte	.LFE193-.LFB193
	.4byte	.LFB194
	.4byte	.LFE194-.LFB194
	.4byte	.LFB195
	.4byte	.LFE195-.LFB195
	.4byte	.LFB196
	.4byte	.LFE196-.LFB196
	.4byte	.LFB197
	.4byte	.LFE197-.LFB197
	.4byte	.LFB198
	.4byte	.LFE198-.LFB198
	.4byte	.LFB199
	.4byte	.LFE199-.LFB199
	.4byte	.LFB200
	.4byte	.LFE200-.LFB200
	.4byte	.LFB201
	.4byte	.LFE201-.LFB201
	.4byte	.LFB202
	.4byte	.LFE202-.LFB202
	.4byte	.LFB203
	.4byte	.LFE203-.LFB203
	.4byte	.LFB204
	.4byte	.LFE204-.LFB204
	.4byte	.LFB205
	.4byte	.LFE205-.LFB205
	.4byte	.LFB206
	.4byte	.LFE206-.LFB206
	.4byte	.LFB207
	.4byte	.LFE207-.LFB207
	.4byte	.LFB208
	.4byte	.LFE208-.LFB208
	.4byte	.LFB209
	.4byte	.LFE209-.LFB209
	.4byte	.LFB210
	.4byte	.LFE210-.LFB210
	.4byte	.LFB211
	.4byte	.LFE211-.LFB211
	.4byte	.LFB286
	.4byte	.LFE286-.LFB286
	.4byte	.LFB287
	.4byte	.LFE287-.LFB287
	.4byte	.LFB288
	.4byte	.LFE288-.LFB288
	.4byte	0
	.4byte	0
	.section	.debug_ranges,"",%progbits
.Ldebug_ranges0:
	.4byte	.LFB138
	.4byte	.LFE138
	.4byte	.LFB164
	.4byte	.LFE164
	.4byte	.LFB165
	.4byte	.LFE165
	.4byte	.LFB166
	.4byte	.LFE166
	.4byte	.LFB167
	.4byte	.LFE167
	.4byte	.LFB168
	.4byte	.LFE168
	.4byte	.LFB169
	.4byte	.LFE169
	.4byte	.LFB170
	.4byte	.LFE170
	.4byte	.LFB171
	.4byte	.LFE171
	.4byte	.LFB172
	.4byte	.LFE172
	.4byte	.LFB173
	.4byte	.LFE173
	.4byte	.LFB174
	.4byte	.LFE174
	.4byte	.LFB175
	.4byte	.LFE175
	.4byte	.LFB176
	.4byte	.LFE176
	.4byte	.LFB177
	.4byte	.LFE177
	.4byte	.LFB178
	.4byte	.LFE178
	.4byte	.LFB179
	.4byte	.LFE179
	.4byte	.LFB180
	.4byte	.LFE180
	.4byte	.LFB181
	.4byte	.LFE181
	.4byte	.LFB182
	.4byte	.LFE182
	.4byte	.LFB183
	.4byte	.LFE183
	.4byte	.LFB184
	.4byte	.LFE184
	.4byte	.LFB185
	.4byte	.LFE185
	.4byte	.LFB186
	.4byte	.LFE186
	.4byte	.LFB187
	.4byte	.LFE187
	.4byte	.LFB188
	.4byte	.LFE188
	.4byte	.LFB189
	.4byte	.LFE189
	.4byte	.LFB190
	.4byte	.LFE190
	.4byte	.LFB191
	.4byte	.LFE191
	.4byte	.LFB192
	.4byte	.LFE192
	.4byte	.LFB193
	.4byte	.LFE193
	.4byte	.LFB194
	.4byte	.LFE194
	.4byte	.LFB195
	.4byte	.LFE195
	.4byte	.LFB196
	.4byte	.LFE196
	.4byte	.LFB197
	.4byte	.LFE197
	.4byte	.LFB198
	.4byte	.LFE198
	.4byte	.LFB199
	.4byte	.LFE199
	.4byte	.LFB200
	.4byte	.LFE200
	.4byte	.LFB201
	.4byte	.LFE201
	.4byte	.LFB202
	.4byte	.LFE202
	.4byte	.LFB203
	.4byte	.LFE203
	.4byte	.LFB204
	.4byte	.LFE204
	.4byte	.LFB205
	.4byte	.LFE205
	.4byte	.LFB206
	.4byte	.LFE206
	.4byte	.LFB207
	.4byte	.LFE207
	.4byte	.LFB208
	.4byte	.LFE208
	.4byte	.LFB209
	.4byte	.LFE209
	.4byte	.LFB210
	.4byte	.LFE210
	.4byte	.LFB211
	.4byte	.LFE211
	.4byte	.LFB286
	.4byte	.LFE286
	.4byte	.LFB287
	.4byte	.LFE287
	.4byte	.LFB288
	.4byte	.LFE288
	.4byte	0
	.4byte	0
	.section	.debug_line,"",%progbits
.Ldebug_line0:
	.section	.debug_str,"MS",%progbits,1
.LASF31:
	.ascii	"EVENTS_ACQUIRED\000"
.LASF130:
	.ascii	"SD_POWER_USBREMOVED_ENABLE\000"
.LASF52:
	.ascii	"TASKS_CLEAR\000"
.LASF7:
	.ascii	"int8_t\000"
.LASF221:
	.ascii	"m_tx_buf\000"
.LASF318:
	.ascii	"p_reset_reason\000"
.LASF188:
	.ascii	"NRFX_SPIS3_INST_IDX\000"
.LASF6:
	.ascii	"size_t\000"
.LASF206:
	.ascii	"irq_priority\000"
.LASF194:
	.ascii	"evt_type\000"
.LASF174:
	.ascii	"NRF_GPIO_PIN_H0S1\000"
.LASF310:
	.ascii	"sd_power_pof_enable\000"
.LASF11:
	.ascii	"int32_t\000"
.LASF146:
	.ascii	"request\000"
.LASF302:
	.ascii	"sd_power_usbregstatus_get\000"
.LASF334:
	.ascii	"/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0."
	.ascii	"0_src/examples/beaconing\000"
.LASF263:
	.ascii	"p_channel_msk\000"
.LASF73:
	.ascii	"copy_sd\000"
.LASF232:
	.ascii	"functional_dataLen\000"
.LASF239:
	.ascii	"log_timestamp_get\000"
.LASF297:
	.ascii	"sd_power_ram_power_set\000"
.LASF207:
	.ascii	"nrfx_spis_config_t\000"
.LASF132:
	.ascii	"SVC_SOC_LAST\000"
.LASF295:
	.ascii	"sd_power_ram_power_clr\000"
.LASF157:
	.ascii	"p_key\000"
.LASF208:
	.ascii	"nrf_drv_spis_t\000"
.LASF35:
	.ascii	"INTENSET\000"
.LASF36:
	.ascii	"INTENCLR\000"
.LASF179:
	.ascii	"NRF_GPIO_PIN_S0D1\000"
.LASF131:
	.ascii	"SD_POWER_USBREGSTATUS_GET\000"
.LASF100:
	.ascii	"SD_RAND_APPLICATION_VECTOR_GET\000"
.LASF181:
	.ascii	"nrf_gpio_pin_drive_t\000"
.LASF102:
	.ascii	"SD_POWER_SYSTEM_OFF\000"
.LASF126:
	.ascii	"SD_EVT_GET\000"
.LASF236:
	.ascii	"sd_protected_register_write\000"
.LASF119:
	.ascii	"SD_CLOCK_HFCLK_IS_RUNNING\000"
.LASF189:
	.ascii	"NRFX_SPIS_ENABLED_COUNT\000"
.LASF89:
	.ascii	"SD_PPI_GROUP_TASK_DISABLE\000"
.LASF201:
	.ascii	"csn_pin\000"
.LASF143:
	.ascii	"request_type\000"
.LASF0:
	.ascii	"long int\000"
.LASF145:
	.ascii	"p_next\000"
.LASF245:
	.ascii	"sd_flash_write\000"
.LASF121:
	.ascii	"SD_ECB_BLOCK_ENCRYPT\000"
.LASF155:
	.ascii	"ciphertext\000"
.LASF261:
	.ascii	"sd_ppi_group_get\000"
.LASF205:
	.ascii	"miso_drive\000"
.LASF247:
	.ascii	"p_src\000"
.LASF280:
	.ascii	"p_is_running\000"
.LASF122:
	.ascii	"SD_ECB_BLOCKS_ENCRYPT\000"
.LASF251:
	.ascii	"sd_evt_get\000"
.LASF154:
	.ascii	"cleartext\000"
.LASF123:
	.ascii	"SD_RADIO_SESSION_OPEN\000"
.LASF286:
	.ascii	"sd_power_gpregret_get\000"
.LASF246:
	.ascii	"p_dst\000"
.LASF270:
	.ascii	"evt_endpoint\000"
.LASF274:
	.ascii	"sd_ppi_channel_enable_set\000"
.LASF203:
	.ascii	"bit_order\000"
.LASF225:
	.ascii	"tx_data\000"
.LASF272:
	.ascii	"sd_ppi_channel_enable_clr\000"
.LASF204:
	.ascii	"csn_pullup\000"
.LASF8:
	.ascii	"signed char\000"
.LASF9:
	.ascii	"uint8_t\000"
.LASF266:
	.ascii	"sd_ppi_group_task_disable\000"
.LASF175:
	.ascii	"NRF_GPIO_PIN_S0H1\000"
.LASF319:
	.ascii	"sd_rand_application_vector_get\000"
.LASF38:
	.ascii	"SEMSTAT\000"
.LASF147:
	.ascii	"extend\000"
.LASF26:
	.ascii	"RESERVED1\000"
.LASF3:
	.ascii	"unsigned char\000"
.LASF30:
	.ascii	"RESERVED3\000"
.LASF32:
	.ascii	"RESERVED4\000"
.LASF34:
	.ascii	"RESERVED5\000"
.LASF37:
	.ascii	"RESERVED6\000"
.LASF39:
	.ascii	"RESERVED7\000"
.LASF41:
	.ascii	"RESERVED8\000"
.LASF43:
	.ascii	"RESERVED9\000"
.LASF312:
	.ascii	"sd_power_system_off\000"
.LASF200:
	.ascii	"sck_pin\000"
.LASF243:
	.ascii	"sd_flash_page_erase\000"
.LASF220:
	.ascii	"m_tx_length\000"
.LASF234:
	.ascii	"p_register\000"
.LASF85:
	.ascii	"SD_PPI_CHANNEL_ENABLE_SET\000"
.LASF242:
	.ascii	"p_radio_signal_callback\000"
.LASF86:
	.ascii	"SD_PPI_CHANNEL_ENABLE_CLR\000"
.LASF224:
	.ascii	"_Bool\000"
.LASF33:
	.ascii	"SHORTS\000"
.LASF67:
	.ascii	"bl_src\000"
.LASF127:
	.ascii	"SD_TEMP_GET\000"
.LASF28:
	.ascii	"RESERVED2\000"
.LASF172:
	.ascii	"nrf_gpio_pin_pull_t\000"
.LASF228:
	.ascii	"spis_start\000"
.LASF1:
	.ascii	"char\000"
.LASF216:
	.ascii	"sen_data\000"
.LASF265:
	.ascii	"channel_msk\000"
.LASF197:
	.ascii	"nrfx_spis_evt_t\000"
.LASF285:
	.ascii	"sd_power_dcdc_mode_set\000"
.LASF110:
	.ascii	"SD_POWER_RAM_POWER_GET\000"
.LASF304:
	.ascii	"sd_power_usbremoved_enable\000"
.LASF156:
	.ascii	"nrf_ecb_hal_data_t\000"
.LASF257:
	.ascii	"p_ecb_data\000"
.LASF128:
	.ascii	"SD_POWER_USBPWRRDY_ENABLE\000"
.LASF80:
	.ascii	"sd_mbr_command_t\000"
.LASF244:
	.ascii	"page_number\000"
.LASF333:
	.ascii	"/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0."
	.ascii	"0_src/examples/beaconing/src/spis.c\000"
.LASF316:
	.ascii	"reset_reason_clr_msk\000"
.LASF260:
	.ascii	"distance\000"
.LASF252:
	.ascii	"p_evt_id\000"
.LASF279:
	.ascii	"sd_clock_hfclk_is_running\000"
.LASF195:
	.ascii	"rx_amount\000"
.LASF142:
	.ascii	"normal\000"
.LASF315:
	.ascii	"sd_power_reset_reason_clr\000"
.LASF214:
	.ascii	"tx_data_buf\000"
.LASF267:
	.ascii	"sd_ppi_group_task_enable\000"
.LASF50:
	.ascii	"TASKS_START\000"
.LASF18:
	.ascii	"MAXCNT\000"
.LASF275:
	.ascii	"channel_enable_set_msk\000"
.LASF190:
	.ascii	"NRFX_SPIS_BUFFERS_SET_DONE\000"
.LASF74:
	.ascii	"compare\000"
.LASF296:
	.ascii	"ram_powerclr\000"
.LASF62:
	.ascii	"NRF_RTC_Type\000"
.LASF98:
	.ascii	"SD_RAND_APPLICATION_POOL_CAPACITY_GET\000"
.LASF23:
	.ascii	"RESERVED\000"
.LASF82:
	.ascii	"NRF_SOC_SVCS\000"
.LASF56:
	.ascii	"EVENTS_COMPARE\000"
.LASF311:
	.ascii	"pof_enable\000"
.LASF282:
	.ascii	"sd_clock_hfclk_request\000"
.LASF161:
	.ascii	"NRF_SPIS_MODE_0\000"
.LASF162:
	.ascii	"NRF_SPIS_MODE_1\000"
.LASF163:
	.ascii	"NRF_SPIS_MODE_2\000"
.LASF164:
	.ascii	"NRF_SPIS_MODE_3\000"
.LASF253:
	.ascii	"sd_ecb_blocks_encrypt\000"
.LASF293:
	.ascii	"index\000"
.LASF150:
	.ascii	"nrf_radio_signal_callback_t\000"
.LASF250:
	.ascii	"p_temp\000"
.LASF139:
	.ascii	"distance_us\000"
.LASF46:
	.ascii	"CONFIG\000"
.LASF97:
	.ascii	"SD_MUTEX_RELEASE\000"
.LASF68:
	.ascii	"bl_len\000"
.LASF70:
	.ascii	"address\000"
.LASF15:
	.ascii	"MISO\000"
.LASF81:
	.ascii	"NRF_MBR_SVCS\000"
.LASF160:
	.ascii	"nrf_ecb_hal_data_block_t\000"
.LASF118:
	.ascii	"SD_CLOCK_HFCLK_RELEASE\000"
.LASF53:
	.ascii	"TASKS_TRIGOVRFLW\000"
.LASF222:
	.ascii	"m_rx_buf\000"
.LASF305:
	.ascii	"usbremoved_enable\000"
.LASF254:
	.ascii	"block_count\000"
.LASF152:
	.ascii	"soc_ecb_cleartext_t\000"
.LASF255:
	.ascii	"p_data_blocks\000"
.LASF325:
	.ascii	"p_pool_capacity\000"
.LASF55:
	.ascii	"EVENTS_OVRFLW\000"
.LASF29:
	.ascii	"EVENTS_ENDRX\000"
.LASF113:
	.ascii	"SD_POWER_GPREGRET_GET\000"
.LASF193:
	.ascii	"nrfx_spis_evt_type_t\000"
.LASF277:
	.ascii	"p_channel_enable\000"
.LASF21:
	.ascii	"SPIS_RXD_Type\000"
.LASF317:
	.ascii	"sd_power_reset_reason_get\000"
.LASF167:
	.ascii	"NRF_SPIS_BIT_ORDER_LSB_FIRST\000"
.LASF223:
	.ascii	"spis_xfer_done\000"
.LASF66:
	.ascii	"sd_mbr_command_compare_t\000"
.LASF258:
	.ascii	"sd_radio_notification_cfg_set\000"
.LASF5:
	.ascii	"long long int\000"
.LASF75:
	.ascii	"copy_bl\000"
.LASF44:
	.ascii	"PSEL\000"
.LASF129:
	.ascii	"SD_POWER_USBDETECTED_ENABLE\000"
.LASF299:
	.ascii	"sd_power_pof_thresholdvddh_set\000"
.LASF314:
	.ascii	"power_mode\000"
.LASF240:
	.ascii	"sd_radio_session_close\000"
.LASF187:
	.ascii	"NRFX_SPIS2_INST_IDX\000"
.LASF229:
	.ascii	"spis_event_handler\000"
.LASF183:
	.ascii	"drv_inst_idx\000"
.LASF180:
	.ascii	"NRF_GPIO_PIN_H0D1\000"
.LASF134:
	.ascii	"hfclk\000"
.LASF210:
	.ascii	"nrf_drv_spis_event_t\000"
.LASF298:
	.ascii	"ram_powerset\000"
.LASF269:
	.ascii	"channel_num\000"
.LASF103:
	.ascii	"SD_POWER_RESET_REASON_GET\000"
.LASF182:
	.ascii	"p_reg\000"
.LASF144:
	.ascii	"nrf_radio_request_t\000"
.LASF217:
	.ascii	"spis\000"
.LASF233:
	.ascii	"event\000"
.LASF57:
	.ascii	"EVTEN\000"
.LASF165:
	.ascii	"nrf_spis_mode_t\000"
.LASF307:
	.ascii	"usbdetected_enable\000"
.LASF92:
	.ascii	"SD_FLASH_PAGE_ERASE\000"
.LASF2:
	.ascii	"unsigned int\000"
.LASF191:
	.ascii	"NRFX_SPIS_XFER_DONE\000"
.LASF117:
	.ascii	"SD_CLOCK_HFCLK_REQUEST\000"
.LASF290:
	.ascii	"gpregret_msk\000"
.LASF281:
	.ascii	"sd_clock_hfclk_release\000"
.LASF140:
	.ascii	"nrf_radio_request_normal_t\000"
.LASF173:
	.ascii	"NRF_GPIO_PIN_S0S1\000"
.LASF303:
	.ascii	"usbregstatus\000"
.LASF309:
	.ascii	"usbpwrrdy_enable\000"
.LASF133:
	.ascii	"nrf_mutex_t\000"
.LASF96:
	.ascii	"SD_MUTEX_ACQUIRE\000"
.LASF60:
	.ascii	"COUNTER\000"
.LASF141:
	.ascii	"earliest\000"
.LASF278:
	.ascii	"sd_app_evt_wait\000"
.LASF291:
	.ascii	"sd_power_gpregret_set\000"
.LASF230:
	.ascii	"len0\000"
.LASF51:
	.ascii	"TASKS_STOP\000"
.LASF289:
	.ascii	"sd_power_gpregret_clr\000"
.LASF231:
	.ascii	"len1\000"
.LASF330:
	.ascii	"sd_mbr_command\000"
.LASF25:
	.ascii	"TASKS_RELEASE\000"
.LASF335:
	.ascii	"Sen_data\000"
.LASF115:
	.ascii	"SD_POWER_DCDC0_MODE_SET\000"
.LASF300:
	.ascii	"threshold\000"
.LASF159:
	.ascii	"p_ciphertext\000"
.LASF71:
	.ascii	"sd_mbr_command_vector_table_base_set_t\000"
.LASF308:
	.ascii	"sd_power_usbpwrrdy_enable\000"
.LASF320:
	.ascii	"p_buff\000"
.LASF259:
	.ascii	"type\000"
.LASF72:
	.ascii	"sd_mbr_command_irq_forward_address_set_t\000"
.LASF16:
	.ascii	"MOSI\000"
.LASF178:
	.ascii	"NRF_GPIO_PIN_D0H1\000"
.LASF283:
	.ascii	"sd_power_dcdc0_mode_set\000"
.LASF14:
	.ascii	"long double\000"
.LASF116:
	.ascii	"SD_APP_EVT_WAIT\000"
.LASF292:
	.ascii	"sd_power_ram_power_get\000"
.LASF105:
	.ascii	"SD_POWER_POF_ENABLE\000"
.LASF170:
	.ascii	"NRF_GPIO_PIN_PULLDOWN\000"
.LASF264:
	.ascii	"sd_ppi_group_assign\000"
.LASF54:
	.ascii	"EVENTS_TICK\000"
.LASF212:
	.ascii	"g_log_dbg_lvl\000"
.LASF176:
	.ascii	"NRF_GPIO_PIN_H0H1\000"
.LASF138:
	.ascii	"nrf_radio_request_earliest_t\000"
.LASF169:
	.ascii	"NRF_GPIO_PIN_NOPULL\000"
.LASF213:
	.ascii	"SWITCH2SPI\000"
.LASF149:
	.ascii	"nrf_radio_signal_callback_return_param_t\000"
.LASF153:
	.ascii	"soc_ecb_ciphertext_t\000"
.LASF27:
	.ascii	"EVENTS_END\000"
.LASF91:
	.ascii	"SD_PPI_GROUP_GET\000"
.LASF192:
	.ascii	"NRFX_SPIS_EVT_TYPE_MAX\000"
.LASF87:
	.ascii	"SD_PPI_CHANNEL_ASSIGN\000"
.LASF329:
	.ascii	"sd_mutex_new\000"
.LASF284:
	.ascii	"dcdc_mode\000"
.LASF326:
	.ascii	"sd_mutex_release\000"
.LASF241:
	.ascii	"sd_radio_session_open\000"
.LASF248:
	.ascii	"size\000"
.LASF301:
	.ascii	"sd_power_pof_threshold_set\000"
.LASF13:
	.ascii	"long long unsigned int\000"
.LASF79:
	.ascii	"params\000"
.LASF186:
	.ascii	"NRFX_SPIS1_INST_IDX\000"
.LASF78:
	.ascii	"command\000"
.LASF288:
	.ascii	"p_gpregret\000"
.LASF108:
	.ascii	"SD_POWER_RAM_POWER_SET\000"
.LASF76:
	.ascii	"base_set\000"
.LASF321:
	.ascii	"length\000"
.LASF166:
	.ascii	"NRF_SPIS_BIT_ORDER_MSB_FIRST\000"
.LASF109:
	.ascii	"SD_POWER_RAM_POWER_CLR\000"
.LASF332:
	.ascii	"GNU C99 10.3.1 20210621 (release) -fmessage-length="
	.ascii	"0 -std=gnu99 -mcpu=cortex-m4 -mlittle-endian -mfloa"
	.ascii	"t-abi=hard -mfpu=fpv4-sp-d16 -mthumb -mtp=soft -mun"
	.ascii	"aligned-access -g2 -gpubnames -fomit-frame-pointer "
	.ascii	"-fno-dwarf2-cfi-asm -ffunction-sections -fdata-sect"
	.ascii	"ions -fshort-enums -fno-common\000"
.LASF306:
	.ascii	"sd_power_usbdetected_enable\000"
.LASF49:
	.ascii	"NRF_SPIS_Type\000"
.LASF45:
	.ascii	"RESERVED10\000"
.LASF47:
	.ascii	"RESERVED11\000"
.LASF48:
	.ascii	"RESERVED12\000"
.LASF235:
	.ascii	"value\000"
.LASF238:
	.ascii	"p_request\000"
.LASF198:
	.ascii	"miso_pin\000"
.LASF294:
	.ascii	"p_ram_power\000"
.LASF114:
	.ascii	"SD_POWER_DCDC_MODE_SET\000"
.LASF271:
	.ascii	"task_endpoint\000"
.LASF95:
	.ascii	"SD_MUTEX_NEW\000"
.LASF101:
	.ascii	"SD_POWER_MODE_SET\000"
.LASF125:
	.ascii	"SD_RADIO_REQUEST\000"
.LASF137:
	.ascii	"timeout_us\000"
.LASF196:
	.ascii	"tx_amount\000"
.LASF22:
	.ascii	"SPIS_TXD_Type\000"
.LASF148:
	.ascii	"callback_action\000"
.LASF171:
	.ascii	"NRF_GPIO_PIN_PULLUP\000"
.LASF211:
	.ascii	"g_log_dbg_msk\000"
.LASF63:
	.ascii	"sd_mbr_command_copy_sd_t\000"
.LASF40:
	.ascii	"STATUS\000"
.LASF262:
	.ascii	"group_num\000"
.LASF83:
	.ascii	"SD_MBR_COMMAND\000"
.LASF151:
	.ascii	"soc_ecb_key_t\000"
.LASF168:
	.ascii	"nrf_spis_bit_order_t\000"
.LASF24:
	.ascii	"TASKS_ACQUIRE\000"
.LASF158:
	.ascii	"p_cleartext\000"
.LASF61:
	.ascii	"PRESCALER\000"
.LASF276:
	.ascii	"sd_ppi_channel_enable_get\000"
.LASF106:
	.ascii	"SD_POWER_POF_THRESHOLD_SET\000"
.LASF64:
	.ascii	"ptr1\000"
.LASF65:
	.ascii	"ptr2\000"
.LASF69:
	.ascii	"sd_mbr_command_copy_bl_t\000"
.LASF313:
	.ascii	"sd_power_mode_set\000"
.LASF273:
	.ascii	"channel_enable_clr_msk\000"
.LASF218:
	.ascii	"m_rx_length\000"
.LASF107:
	.ascii	"SD_POWER_POF_THRESHOLDVDDH_SET\000"
.LASF215:
	.ascii	"tx_data_len\000"
.LASF10:
	.ascii	"short int\000"
.LASF226:
	.ascii	"spis_config\000"
.LASF324:
	.ascii	"sd_rand_application_pool_capacity_get\000"
.LASF227:
	.ascii	"LOCAL_ERR_CODE\000"
.LASF202:
	.ascii	"mode\000"
.LASF135:
	.ascii	"priority\000"
.LASF136:
	.ascii	"length_us\000"
.LASF84:
	.ascii	"SD_PPI_CHANNEL_ENABLE_GET\000"
.LASF184:
	.ascii	"nrfx_spis_t\000"
.LASF42:
	.ascii	"ENABLE\000"
.LASF327:
	.ascii	"p_mutex\000"
.LASF328:
	.ascii	"sd_mutex_acquire\000"
.LASF249:
	.ascii	"sd_temp_get\000"
.LASF256:
	.ascii	"sd_ecb_block_encrypt\000"
.LASF19:
	.ascii	"AMOUNT\000"
.LASF237:
	.ascii	"sd_radio_request\000"
.LASF185:
	.ascii	"NRFX_SPIS0_INST_IDX\000"
.LASF88:
	.ascii	"SD_PPI_GROUP_TASK_ENABLE\000"
.LASF17:
	.ascii	"SPIS_PSEL_Type\000"
.LASF111:
	.ascii	"SD_POWER_GPREGRET_SET\000"
.LASF112:
	.ascii	"SD_POWER_GPREGRET_CLR\000"
.LASF12:
	.ascii	"uint32_t\000"
.LASF94:
	.ascii	"SD_PROTECTED_REGISTER_WRITE\000"
.LASF287:
	.ascii	"gpregret_id\000"
.LASF120:
	.ascii	"SD_RADIO_NOTIFICATION_CFG_SET\000"
.LASF93:
	.ascii	"SD_FLASH_WRITE\000"
.LASF20:
	.ascii	"LIST\000"
.LASF4:
	.ascii	"short unsigned int\000"
.LASF58:
	.ascii	"EVTENSET\000"
.LASF59:
	.ascii	"EVTENCLR\000"
.LASF209:
	.ascii	"nrf_drv_spis_config_t\000"
.LASF90:
	.ascii	"SD_PPI_GROUP_ASSIGN\000"
.LASF323:
	.ascii	"p_bytes_available\000"
.LASF199:
	.ascii	"mosi_pin\000"
.LASF99:
	.ascii	"SD_RAND_APPLICATION_BYTES_AVAILABLE_GET\000"
.LASF77:
	.ascii	"irq_forward_address_set\000"
.LASF104:
	.ascii	"SD_POWER_RESET_REASON_CLR\000"
.LASF219:
	.ascii	"m_tx_max__length\000"
.LASF124:
	.ascii	"SD_RADIO_SESSION_CLOSE\000"
.LASF331:
	.ascii	"param\000"
.LASF268:
	.ascii	"sd_ppi_channel_assign\000"
.LASF177:
	.ascii	"NRF_GPIO_PIN_D0S1\000"
.LASF322:
	.ascii	"sd_rand_application_bytes_available_get\000"
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
