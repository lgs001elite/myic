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
	.file	"mesh_adv.c"
	.text
	.section	.text.sd_ble_gap_adv_set_configure,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ble_gap_adv_set_configure, %function
sd_ble_gap_adv_set_configure:
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.syntax unified
@ 1878 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s132/headers/ble_gap.h" 1
	svc #114
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	.size	sd_ble_gap_adv_set_configure, .-sd_ble_gap_adv_set_configure
	.section	.text.sd_ble_gap_adv_start,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ble_gap_adv_start, %function
sd_ble_gap_adv_start:
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.syntax unified
@ 1928 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s132/headers/ble_gap.h" 1
	svc #115
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	.size	sd_ble_gap_adv_start, .-sd_ble_gap_adv_start
	.section	.text.sd_ble_gap_adv_stop,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_ble_gap_adv_stop, %function
sd_ble_gap_adv_stop:
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.syntax unified
@ 1944 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s132/headers/ble_gap.h" 1
	svc #116
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	.size	sd_ble_gap_adv_stop, .-sd_ble_gap_adv_stop
	.section	.text.mesh_adv_data_set,"ax",%progbits
	.align	1
	.global	mesh_adv_data_set
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_adv_data_set, %function
mesh_adv_data_set:
	@ args = 0, pretend = 0, frame = 136
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, r7, r8, r9, r10, lr}
	mov	r7, r1
	ldr	r1, .L18
	ldr	r5, .L18+4
	ldrb	r3, [r1]	@ zero_extendqisi2
	ldr	r4, .L18+8
	mov	r6, r0
	ldr	r0, .L18+12
	mov	r8, r2
	rsb	r2, r3, r3, lsl #5
	add	r5, r5, r2
	adds	r3, r3, #1
	add	r2, r2, r0
	sub	sp, sp, #136
	mov	r10, #0
	and	r3, r3, #1
	str	r2, [r4, #8]
	movs	r2, #31
	strb	r3, [r1]
	str	r10, [r4, #4]
	str	r10, [r4, #12]
	strh	r2, [r4, #4]	@ movhi
	strh	r2, [r4, #12]	@ movhi
	mov	r1, r10
	movs	r2, #60
	add	r0, sp, #16
	str	r5, [r4]
	bl	memset
	movs	r3, #6
	add	r2, sp, #4
	strb	r3, [sp, #19]
	str	r2, [sp, #56]
	movs	r3, #1
	movs	r2, #60
	mov	r1, r10
	add	r9, r4, #4
	add	r0, sp, #76
	strb	r3, [sp, #2]
	strh	r3, [sp, #32]	@ movhi
	strb	r3, [sp, #60]
	strh	r6, [sp]	@ movhi
	str	sp, [sp, #36]
	strh	r6, [sp, #4]	@ movhi
	strh	r8, [sp, #8]	@ movhi
	str	r7, [sp, #12]
	bl	memset
	movs	r3, #2
	mov	r2, r9
	mov	r1, r5
	add	r0, sp, #16
	strb	r3, [sp, #76]
	bl	ble_advdata_encode
	cbz	r0, .L5
	bl	app_error_handler_bare
.L5:
	ldr	r2, .L18+16
	ldr	r1, [r4, #8]
	add	r0, sp, #76
	bl	ble_advdata_encode
	cbz	r0, .L6
	bl	app_error_handler_bare
.L6:
	ldr	r2, .L18+20
	ldr	r1, .L18+8
	ldr	r0, .L18+24
	bl	sd_ble_gap_adv_set_configure
	cmp	r0, #8
	bne	.L7
	ldr	r1, .L18+8
	ldr	r0, .L18+24
	movs	r2, #0
	bl	sd_ble_gap_adv_set_configure
.L7:
	cbz	r0, .L4
	bl	app_error_handler_bare
.L4:
	add	sp, sp, #136
	@ sp needed
	pop	{r4, r5, r6, r7, r8, r9, r10, pc}
.L19:
	.align	2
.L18:
	.word	.LANCHOR1
	.word	.LANCHOR2
	.word	.LANCHOR0
	.word	.LANCHOR3
	.word	.LANCHOR0+12
	.word	.LANCHOR4
	.word	.LANCHOR5
	.size	mesh_adv_data_set, .-mesh_adv_data_set
	.section	.text.mesh_adv_params_set,"ax",%progbits
	.align	1
	.global	mesh_adv_params_set
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_adv_params_set, %function
mesh_adv_params_set:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	cmp	r0, #655360
	bcs	.L23
	movs	r3, #10
	udiv	r3, r0, r3
	cbz	r0, .L22
.L21:
	cmp	r3, #1
	it	cc
	movcc	r3, #1
.L22:
	ldr	r2, .L27
	strh	r3, [r2, #12]	@ movhi
	str	r1, [r2, #8]
	bx	lr
.L23:
	movw	r3, #65535
	b	.L21
.L28:
	.align	2
.L27:
	.word	.LANCHOR4
	.size	mesh_adv_params_set, .-mesh_adv_params_set
	.section	.text.mesh_adv_start,"ax",%progbits
	.align	1
	.global	mesh_adv_start
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_adv_start, %function
mesh_adv_start:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, lr}
	ldr	r3, .L34
	movs	r1, #1
	ldrb	r0, [r3]	@ zero_extendqisi2
	bl	sd_ble_gap_adv_start
	cbz	r0, .L30
	bl	app_error_handler_bare
.L30:
	pop	{r3, lr}
	movs	r0, #0
	b	timeslot_restart
.L35:
	.align	2
.L34:
	.word	.LANCHOR5
	.size	mesh_adv_start, .-mesh_adv_start
	.section	.text.mesh_adv_stop,"ax",%progbits
	.align	1
	.global	mesh_adv_stop
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_adv_stop, %function
mesh_adv_stop:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, lr}
	ldr	r3, .L38
	ldrb	r0, [r3]	@ zero_extendqisi2
	bl	sd_ble_gap_adv_stop
	cbz	r0, .L36
	pop	{r3, lr}
	b	app_error_handler_bare
.L36:
	pop	{r3, pc}
.L39:
	.align	2
.L38:
	.word	.LANCHOR5
	.size	mesh_adv_stop, .-mesh_adv_stop
	.section	.bss.m_adv_set_index,"aw",%nobits
	.set	.LANCHOR1,. + 0
	.type	m_adv_set_index, %object
	.size	m_adv_set_index, 1
m_adv_set_index:
	.space	1
	.section	.bss.m_advdata_raw,"aw",%nobits
	.set	.LANCHOR2,. + 0
	.type	m_advdata_raw, %object
	.size	m_advdata_raw, 62
m_advdata_raw:
	.space	62
	.section	.bss.m_gap_adv_data,"aw",%nobits
	.align	2
	.set	.LANCHOR0,. + 0
	.type	m_gap_adv_data, %object
	.size	m_gap_adv_data, 16
m_gap_adv_data:
	.space	16
	.section	.bss.m_srdata_raw,"aw",%nobits
	.set	.LANCHOR3,. + 0
	.type	m_srdata_raw, %object
	.size	m_srdata_raw, 62
m_srdata_raw:
	.space	62
	.section	.data.m_adv_handle,"aw"
	.set	.LANCHOR5,. + 0
	.type	m_adv_handle, %object
	.size	m_adv_handle, 1
m_adv_handle:
	.byte	-1
	.section	.data.m_adv_params,"aw"
	.align	2
	.set	.LANCHOR4,. + 0
	.type	m_adv_params, %object
	.size	m_adv_params, 24
m_adv_params:
	.byte	1
	.space	1
	.space	6
	.word	320
	.short	0
	.space	10
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
