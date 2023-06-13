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
	.file	"spis.c"
	.text
	.section	.text.sd_app_evt_wait,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	sd_app_evt_wait, %function
sd_app_evt_wait:
	@ Naked Function: prologue and epilogue provided by programmer.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	.syntax unified
@ 748 "../../../nRF5_SDK_17.0.2_d674dde/components/softdevice/s140/headers/nrf_soc.h" 1
	svc #65
bx r14
@ 0 "" 2
	.thumb
	.syntax unified
	.size	sd_app_evt_wait, .-sd_app_evt_wait
	.section	.rodata.spis_event_handler.str1.1,"aMS",%progbits,1
.LC1:
	.ascii	"/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0."
	.ascii	"0_src/examples/beaconing/src/spis.c\000"
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
	@ args = 0, pretend = 0, frame = 16
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	sub	sp, sp, #32
	add	r3, sp, #32
	stmdb	r3, {r0, r1, r2}
	ldrb	r3, [sp, #20]	@ zero_extendqisi2
	cmp	r3, #1
	bne	.L2
	ldr	r2, .L13
	ldr	r4, .L13+4
	strb	r3, [r2]
	ldr	r3, .L13+8
	ldr	r3, [r3]
	tst	r3, #16384
	beq	.L5
	ldr	r3, .L13+12
	ldr	r3, [r3]
	cmp	r3, #3
	ble	.L5
	ldr	r2, [r4]
	ldr	r3, .L13+16
	ldrb	r1, [r2]	@ zero_extendqisi2
	ldr	r3, [r3, #1284]
	strd	r2, r1, [sp, #4]
	ldr	r2, .L13+20
	str	r2, [sp]
	ldr	r1, .L13+24
	movs	r2, #40
	movs	r0, #4
	bl	log_printf
.L5:
	ldr	r0, [r4]
	ldrb	r3, [r0, #2]	@ zero_extendqisi2
	ldrb	r1, [r0, #1]	@ zero_extendqisi2
	add	r1, r3, r1, lsl #4
	bl	spis_setfrom_master
	ldr	r3, [r4]
	ldrb	r3, [r3]	@ zero_extendqisi2
	cbz	r3, .L2
	ldr	r3, .L13+28
	movs	r2, #0
	strb	r2, [r3]
.L2:
	add	sp, sp, #32
	@ sp needed
	pop	{r4, pc}
.L14:
	.align	2
.L13:
	.word	.LANCHOR0
	.word	.LANCHOR1
	.word	g_log_dbg_msk
	.word	g_log_dbg_lvl
	.word	1073811456
	.word	.LC2
	.word	.LC1+80
	.word	.LANCHOR2
	.size	spis_event_handler, .-spis_event_handler
	.section	.rodata.spis_start.str1.1,"aMS",%progbits,1
.LC3:
	.ascii	"spis_start\012\000"
.LC4:
	.ascii	"tx_data.tx_data_buf: %s, addr: %x\012\000"
	.section	.text.spis_start,"ax",%progbits
	.align	1
	.global	spis_start
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	spis_start, %function
spis_start:
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, r7, r8, r9, lr}
	ldr	r5, .L40
	ldr	r3, [r5]
	lsls	r4, r3, #17
	sub	sp, sp, #52
	bpl	.L16
	ldr	r3, .L40+4
	ldr	r3, [r3]
	cmp	r3, #3
	ble	.L16
	ldr	r3, .L40+8
	ldr	r2, .L40+12
	ldr	r3, [r3, #1284]
	ldr	r1, .L40+16
	str	r2, [sp]
	movs	r0, #4
	movs	r2, #59
	bl	log_printf
.L16:
	add	r0, sp, #16
	bl	spis_getfrom_slave
	movs	r0, #100
	ldr	r4, [sp, #16]
	ldr	r6, .L40+20
	bl	malloc
	str	r0, [r6]
	cmp	r0, #0
	beq	.L15
	ldr	r3, [r5]
	lsls	r0, r3, #17
	bpl	.L18
	ldr	r3, .L40+4
	ldr	r3, [r3]
	cmp	r3, #3
	ble	.L18
	ldr	r3, .L40+8
	ldr	r2, .L40+24
	ldr	r3, [r3, #1284]
	ldr	r1, .L40+16
	str	r2, [sp]
	strd	r4, r4, [sp, #4]
	movs	r2, #72
	movs	r0, #4
	bl	log_printf
.L18:
	ldr	r7, .L40+28
	ldr	r2, [sp, #20]
	ldr	r1, [r6]
	str	r2, [r7]
	movs	r3, #0
.L19:
	cmp	r2, r3
	bne	.L20
	ldr	r5, .L40+32
	ldmia	r5!, {r0, r1, r2, r3}
	add	r4, sp, #24
	stmia	r4!, {r0, r1, r2, r3}
	ldm	r5, {r0, r1}
	movs	r3, #31
	stm	r4, {r0, r1}
	str	r3, [sp, #36]
	movs	r1, #30
	movs	r3, #29
	strd	r1, r3, [sp, #24]
	ldr	r2, .L40+36
	ldr	r0, .L40+40
	movs	r3, #26
	add	r1, sp, #24
	str	r3, [sp, #32]
	bl	nrf_drv_spis_init
	cbz	r0, .L21
	bl	app_error_handler_bare
.L21:
	ldr	r9, .L40+52
	ldr	r5, .L40+44
.L22:
	ldrsb	r3, [r9]
	cbnz	r3, .L26
.L15:
	add	sp, sp, #52
	@ sp needed
	pop	{r4, r5, r6, r7, r8, r9, pc}
.L20:
	ldrb	r0, [r4, r3]	@ zero_extendqisi2
	strb	r0, [r1, r3]
	adds	r3, r3, #1
	b	.L19
.L26:
	movs	r0, #100
	bl	malloc
	mov	r8, #100
	ldr	r3, .L40+48
	mov	r2, r8
	movs	r1, #0
	mov	r4, r0
	str	r0, [r3]
	bl	memset
	movs	r3, #0
	strb	r3, [r5]
	ldr	r2, [r7]
	ldr	r1, [r6]
	ldr	r0, .L40+40
	str	r8, [sp]
	mov	r3, r4
	bl	nrfx_spis_buffers_set
	cbz	r0, .L24
	bl	app_error_handler_bare
.L24:
	ldrb	r3, [r5]	@ zero_extendqisi2
	and	r4, r3, #255
	cmp	r3, #0
	bne	.L22
	bl	sd_app_evt_wait
	mov	r0, r4
	bl	bsp_board_led_invert
	b	.L24
.L41:
	.align	2
.L40:
	.word	g_log_dbg_msk
	.word	g_log_dbg_lvl
	.word	1073811456
	.word	.LC3
	.word	.LC1+80
	.word	.LANCHOR3
	.word	.LC4
	.word	.LANCHOR4
	.word	.LANCHOR5
	.word	spis_event_handler
	.word	.LANCHOR6
	.word	.LANCHOR0
	.word	.LANCHOR1
	.word	.LANCHOR2
	.size	spis_start, .-spis_start
	.global	SWITCH2SPI
	.section .rodata
	.align	2
	.set	.LANCHOR5,. + 0
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
	.section	.bss.SWITCH2SPI,"aw",%nobits
	.set	.LANCHOR2,. + 0
	.type	SWITCH2SPI, %object
	.size	SWITCH2SPI, 1
SWITCH2SPI:
	.space	1
	.section	.bss.m_rx_buf,"aw",%nobits
	.align	2
	.set	.LANCHOR1,. + 0
	.type	m_rx_buf, %object
	.size	m_rx_buf, 4
m_rx_buf:
	.space	4
	.section	.bss.m_tx_buf,"aw",%nobits
	.align	2
	.set	.LANCHOR3,. + 0
	.type	m_tx_buf, %object
	.size	m_tx_buf, 4
m_tx_buf:
	.space	4
	.section	.bss.m_tx_length,"aw",%nobits
	.align	2
	.set	.LANCHOR4,. + 0
	.type	m_tx_length, %object
	.size	m_tx_length, 4
m_tx_length:
	.space	4
	.section	.bss.spis_xfer_done,"aw",%nobits
	.set	.LANCHOR0,. + 0
	.type	spis_xfer_done, %object
	.size	spis_xfer_done, 1
spis_xfer_done:
	.space	1
	.section	.rodata.spis,"a"
	.align	2
	.set	.LANCHOR6,. + 0
	.type	spis, %object
	.size	spis, 8
spis:
	.word	1073758208
	.byte	1
	.space	3
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
