	.cpu cortex-m4
	.eabi_attribute 27, 1
	.eabi_attribute 28, 1
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 1
	.eabi_attribute 30, 4
	.eabi_attribute 34, 1
	.eabi_attribute 18, 4
	.file	"ble_softdevice_support.c"
	.text
	.section	.text.sd_ble_enable,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ble_enable, %function
sd_ble_enable:
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.syntax unified
@ 434 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/ble.h" 1
	svc #96
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	.size	sd_ble_enable, .-sd_ble_enable
	.section	.text.sd_ble_cfg_set,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ble_cfg_set, %function
sd_ble_cfg_set:
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.syntax unified
@ 470 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/ble.h" 1
	svc #105
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	.size	sd_ble_cfg_set, .-sd_ble_cfg_set
	.section	.text.on_sd_evt,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	on_sd_evt, %function
on_sd_evt:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	b	nrf_mesh_on_sd_evt
	.size	on_sd_evt, .-on_sd_evt
	.section	.rodata.ble_stack_init.str1.1,"aMS",%progbits,1
.LC0:
	.ascii	"/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0."
	.ascii	"0_src/examples/common/src/ble_softdevice_support.c\000"
.LC1:
	.ascii	"sd_ble_enable: app_ram_base should be adjusted to 0"
	.ascii	"x%0x\012\000"
	.section	.text.ble_stack_init,"ax",%progbits
	.align	1
	.global	ble_stack_init
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	ble_stack_init, %function
ble_stack_init:
	@ args = 0, pretend = 0, frame = 24
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	sub	sp, sp, #32
	bl	nrf_sdh_enable_request
	cbz	r0, .L5
	bl	app_error_handler_bare
.L5:
	ldr	r3, .L25
	str	r3, [sp, #12]
	movs	r4, #0
	ldr	r2, [sp, #12]
	str	r2, [sp, #16]
	add	r1, sp, #20
	movs	r0, #1
	strd	r4, r4, [sp, #20]
	str	r4, [sp, #28]
	bl	sd_ble_cfg_set
	cbz	r0, .L6
	bl	app_error_handler_bare
.L6:
	movs	r3, #248
	ldr	r2, [sp, #16]
	str	r3, [sp, #20]
	add	r1, sp, #20
	movs	r0, #161
	strd	r4, r4, [sp, #24]
	bl	sd_ble_cfg_set
	cbz	r0, .L7
	bl	app_error_handler_bare
.L7:
	add	r0, sp, #16
	bl	sd_ble_enable
	ldr	r2, [sp, #16]
	ldr	r3, [sp, #12]
	cmp	r2, r3
	mov	r4, r0
	beq	.L8
	ldr	r3, .L25+4
	ldr	r3, [r3]
	lsls	r3, r3, #17
	bpl	.L8
	ldr	r3, .L25+8
	ldr	r3, [r3]
	cmp	r3, #1
	ble	.L8
	ldr	r3, .L25+12
	ldr	r1, .L25+16
	ldr	r3, [r3, #1284]
	str	r2, [sp, #4]
	ldr	r2, .L25+20
	str	r2, [sp]
	movs	r0, #2
	movs	r2, #171
	bl	log_printf
.L8:
	cbz	r4, .L4
	mov	r0, r4
	bl	app_error_handler_bare
.L4:
	add	sp, sp, #32
	@ sp needed
	pop	{r4, pc}
.L26:
	.align	2
.L25:
	.word	__data_start__
	.word	g_log_dbg_msk
	.word	g_log_dbg_lvl
	.word	1073811456
	.word	.LC0+77
	.word	.LC1
	.size	ble_stack_init, .-ble_stack_init
	.section	.sdh_soc_observers0,"a"
	.align	2
	.type	mesh_observer.0, %object
	.size	mesh_observer.0, 8
mesh_observer.0:
	.word	on_sd_evt
	.word	0
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
