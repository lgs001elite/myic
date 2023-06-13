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
	.file	"simple_hal.c"
	.text
	.section	.text.button_event_handler,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	button_event_handler, %function
button_event_handler:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, r6, r7, r8, r9, lr}
	ldr	r7, .L8
	ldr	r8, .L8+8
	ldr	r9, .L8+12
	mov	r5, r0
	movs	r4, #0
.L6:
	ldrb	r3, [r7], #1	@ zero_extendqisi2
	cmp	r3, r5
	bne	.L3
	ldr	r6, [r8]
	bl	timer_now
	subs	r3, r6, r0
	it	mi
	submi	r3, r0, r6
	cmp	r3, r9
	bls	.L3
	bl	timer_now
	ldr	r3, .L8+4
	str	r0, [r8]
	ldr	r3, [r3]
	mov	r0, r4
	blx	r3
.L3:
	adds	r4, r4, #1
	cmp	r4, #4
	bne	.L6
	pop	{r3, r4, r5, r6, r7, r8, r9, pc}
.L9:
	.align	2
.L8:
	.word	.LANCHOR0
	.word	.LANCHOR2
	.word	.LANCHOR1
	.word	400000
	.size	button_event_handler, .-button_event_handler
	.section	.text.hal_led_pin_get,"ax",%progbits
	.align	1
	.global	hal_led_pin_get
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	hal_led_pin_get, %function
hal_led_pin_get:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	cmp	r0, #31
	itet	hi
	ldrhi	r3, .L13
	movls	r3, #1342177280
	andhi	r0, r0, #31
	ldr	r3, [r3, #1284]
	lsr	r0, r3, r0
	mvns	r0, r0
	and	r0, r0, #1
	bx	lr
.L14:
	.align	2
.L13:
	.word	1342178048
	.size	hal_led_pin_get, .-hal_led_pin_get
	.section	.text.hal_led_pin_set,"ax",%progbits
	.align	1
	.global	hal_led_pin_set
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	hal_led_pin_set, %function
hal_led_pin_set:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	cbz	r1, .L16
	b	nrfx_gpiote_out_clear
.L16:
	b	nrfx_gpiote_out_set
	.size	hal_led_pin_set, .-hal_led_pin_set
	.section	.text.led_timeout_handler,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	led_timeout_handler, %function
led_timeout_handler:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, r6, r7, r8, r9, lr}
	ldr	r5, .L32
	ldr	r0, [r5]
	cbnz	r0, .L18
	bl	app_error_handler_bare
.L18:
	ldr	r6, .L32+4
	ldr	r9, .L32+16
	ldr	r7, [r6]
	movs	r4, #0
	mov	r8, #1
.L20:
	lsl	r3, r8, r4
	tst	r3, r7
	beq	.L19
	ldrb	r2, [r4, r9]	@ zero_extendqisi2
	mov	r0, r2
	bl	hal_led_pin_get
	eor	r0, r0, #1
	uxtb	r1, r0
	mov	r0, r2
	bl	hal_led_pin_set
.L19:
	adds	r4, r4, #1
	cmp	r4, #4
	bne	.L20
	ldr	r4, [r5]
	subs	r4, r4, #1
	str	r4, [r5]
	cbnz	r4, .L17
	ldr	r0, .L32+8
	ldr	r7, .L32+12
	ldr	r8, .L32+16
	bl	app_timer_stop
	movs	r5, #1
.L23:
	ldr	r2, [r6]
	lsl	r3, r5, r4
	tst	r3, r2
	beq	.L22
	ldr	r1, [r7]
	ldrb	r0, [r8, r4]	@ zero_extendqisi2
	lsrs	r1, r1, r4
	and	r1, r1, #1
	bl	hal_led_pin_set
.L22:
	adds	r4, r4, #1
	cmp	r4, #4
	bne	.L23
.L17:
	pop	{r3, r4, r5, r6, r7, r8, r9, pc}
.L33:
	.align	2
.L32:
	.word	.LANCHOR3
	.word	.LANCHOR4
	.word	.LANCHOR6
	.word	.LANCHOR7
	.word	.LANCHOR5
	.size	led_timeout_handler, .-led_timeout_handler
	.section	.text.hal_led_mask_set,"ax",%progbits
	.align	1
	.global	hal_led_mask_set
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	hal_led_mask_set, %function
hal_led_mask_set:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, r7, r8, lr}
	ldr	r7, .L41
	mov	r5, r0
	mov	r8, r1
	movs	r4, #0
	movs	r6, #1
.L36:
	lsl	r3, r6, r4
	tst	r3, r5
	beq	.L35
	ldrb	r0, [r7, r4]	@ zero_extendqisi2
	mov	r1, r8
	bl	hal_led_pin_set
.L35:
	adds	r4, r4, #1
	cmp	r4, #4
	bne	.L36
	pop	{r4, r5, r6, r7, r8, pc}
.L42:
	.align	2
.L41:
	.word	.LANCHOR5
	.size	hal_led_mask_set, .-hal_led_mask_set
	.global	__aeabi_uldivmod
	.global	__aeabi_ldivmod
	.section	.text.hal_led_blink_ms,"ax",%progbits
	.align	1
	.global	hal_led_blink_ms
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	hal_led_blink_ms, %function
hal_led_blink_ms:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, r7, r8, lr}
	mov	r5, r0
	mov	r4, r1
	cbz	r2, .L43
	cmp	r1, #19
	bls	.L43
	ldr	r6, .L53
	ldr	r3, .L53+4
	ldr	r8, .L53+16
	str	r0, [r6]
	lsls	r2, r2, #1
	subs	r2, r2, #1
	movs	r1, #0
	str	r2, [r3]
	movs	r7, #1
	mov	r2, r1
.L48:
	lsl	r3, r7, r2
	tst	r3, r5
	beq	.L47
	ldrb	r0, [r8, r2]	@ zero_extendqisi2
	bl	hal_led_pin_get
	lsls	r0, r0, r2
	orrs	r1, r1, r0
.L47:
	adds	r2, r2, #1
	cmp	r2, #4
	bne	.L48
	ldr	r3, .L53+8
	movs	r5, #0
	str	r1, [r3]
	mov	r7, #32768
	mov	r0, #500
	mov	r1, r5
	mov	r2, #1000
	movs	r3, #0
	umlal	r0, r1, r4, r7
	bl	__aeabi_uldivmod
	mov	r2, r5
	mov	r1, r0
	ldr	r0, .L53+12
	bl	app_timer_start
	cbnz	r0, .L43
	ldr	r0, [r6]
	movs	r1, #1
	pop	{r4, r5, r6, r7, r8, lr}
	b	hal_led_mask_set
.L43:
	pop	{r4, r5, r6, r7, r8, pc}
.L54:
	.align	2
.L53:
	.word	.LANCHOR4
	.word	.LANCHOR3
	.word	.LANCHOR7
	.word	.LANCHOR6
	.word	.LANCHOR5
	.size	hal_led_blink_ms, .-hal_led_blink_ms
	.section	.text.hal_led_blink_stop,"ax",%progbits
	.align	1
	.global	hal_led_blink_stop
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	hal_led_blink_stop, %function
hal_led_blink_stop:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, lr}
	ldr	r0, .L56
	bl	app_timer_stop
	ldr	r3, .L56+4
	movs	r1, #0
	ldr	r0, [r3]
	pop	{r3, lr}
	b	hal_led_mask_set
.L57:
	.align	2
.L56:
	.word	.LANCHOR6
	.word	.LANCHOR4
	.size	hal_led_blink_stop, .-hal_led_blink_stop
	.section	.text.hal_leds_init,"ax",%progbits
	.align	1
	.global	hal_leds_init
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	hal_leds_init, %function
hal_leds_init:
	@ args = 0, pretend = 0, frame = 8
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, r4, r5, lr}
	bl	nrfx_gpiote_is_init
	cbnz	r0, .L60
	bl	nrfx_gpiote_init
	cbz	r0, .L60
	bl	app_error_handler_bare
.L60:
	movs	r4, #0
	movs	r3, #1
	ldr	r5, .L75
	strh	r4, [sp, #4]	@ movhi
	strb	r4, [sp, #6]
	strb	r3, [sp, #5]
.L63:
	ldrb	r0, [r5], #1	@ zero_extendqisi2
	add	r1, sp, #4
	bl	nrfx_gpiote_out_init
	cbz	r0, .L62
	bl	app_error_handler_bare
.L62:
	adds	r4, r4, #1
	cmp	r4, #4
	bne	.L63
	ldr	r2, .L75+4
	ldr	r0, .L75+8
	movs	r1, #1
	bl	app_timer_create
	cbz	r0, .L58
	bl	app_error_handler_bare
.L58:
	add	sp, sp, #12
	@ sp needed
	pop	{r4, r5, pc}
.L76:
	.align	2
.L75:
	.word	.LANCHOR5
	.word	led_timeout_handler
	.word	.LANCHOR8
	.size	hal_leds_init, .-hal_leds_init
	.section	.text.hal_buttons_init,"ax",%progbits
	.align	1
	.global	hal_buttons_init
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	hal_buttons_init, %function
hal_buttons_init:
	@ args = 0, pretend = 0, frame = 8
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, r4, r5, r6, r7, lr}
	cbz	r0, .L84
	ldr	r3, .L92
	str	r0, [r3]
	bl	nrfx_gpiote_is_init
	cbnz	r0, .L80
	bl	nrfx_gpiote_init
	cbz	r0, .L80
	bl	app_error_handler_bare
.L80:
	ldr	r3, .L92+4
	ldr	r6, .L92+8
	ldrh	r2, [r3]	@ unaligned
	ldr	r7, .L92+12
	ldrb	r3, [r3, #2]	@ zero_extendqisi2
	strh	r2, [sp, #4]	@ unaligned
	strb	r3, [sp, #6]
	movs	r4, #0
.L83:
	ldrb	r5, [r6], #1	@ zero_extendqisi2
	mov	r2, r7
	add	r1, sp, #4
	mov	r0, r5
	bl	nrfx_gpiote_in_init
	cbz	r0, .L82
	bl	app_error_handler_bare
.L82:
	movs	r1, #1
	mov	r0, r5
	adds	r4, r4, #1
	bl	nrfx_gpiote_in_event_enable
	cmp	r4, #4
	bne	.L83
	movs	r0, #0
.L77:
	add	sp, sp, #12
	@ sp needed
	pop	{r4, r5, r6, r7, pc}
.L84:
	movs	r0, #14
	b	.L77
.L93:
	.align	2
.L92:
	.word	.LANCHOR2
	.word	.LANCHOR9
	.word	.LANCHOR0
	.word	button_event_handler
	.size	hal_buttons_init, .-hal_buttons_init
	.section .rodata
	.set	.LANCHOR9,. + 0
.LC0:
	.byte	2
	.byte	3
	.byte	0
	.section	.bss.m_blink_count,"aw",%nobits
	.align	2
	.set	.LANCHOR3,. + 0
	.type	m_blink_count, %object
	.size	m_blink_count, 4
m_blink_count:
	.space	4
	.section	.bss.m_blink_mask,"aw",%nobits
	.align	2
	.set	.LANCHOR4,. + 0
	.type	m_blink_mask, %object
	.size	m_blink_mask, 4
m_blink_mask:
	.space	4
	.section	.bss.m_blink_timer_data,"aw",%nobits
	.align	2
	.set	.LANCHOR6,. + 0
	.type	m_blink_timer_data, %object
	.size	m_blink_timer_data, 32
m_blink_timer_data:
	.space	32
	.section	.bss.m_button_handler_cb,"aw",%nobits
	.align	2
	.set	.LANCHOR2,. + 0
	.type	m_button_handler_cb, %object
	.size	m_button_handler_cb, 4
m_button_handler_cb:
	.space	4
	.section	.bss.m_last_button_press,"aw",%nobits
	.align	2
	.set	.LANCHOR1,. + 0
	.type	m_last_button_press, %object
	.size	m_last_button_press, 4
m_last_button_press:
	.space	4
	.section	.bss.m_prev_state,"aw",%nobits
	.align	2
	.set	.LANCHOR7,. + 0
	.type	m_prev_state, %object
	.size	m_prev_state, 4
m_prev_state:
	.space	4
	.section	.rodata.m_blink_timer,"a"
	.align	2
	.set	.LANCHOR8,. + 0
	.type	m_blink_timer, %object
	.size	m_blink_timer, 4
m_blink_timer:
	.word	m_blink_timer_data
	.section	.rodata.m_buttons_list,"a"
	.set	.LANCHOR0,. + 0
	.type	m_buttons_list, %object
	.size	m_buttons_list, 4
m_buttons_list:
	.ascii	"\013\014\030\031"
	.section	.rodata.m_leds_list,"a"
	.set	.LANCHOR5,. + 0
	.type	m_leds_list, %object
	.size	m_leds_list, 4
m_leds_list:
	.ascii	"\015\016\017\020"
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
