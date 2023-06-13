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
	.file	"mesh_provisionee.c"
	.text
	.section	.text.power_down_evt_handle,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	power_down_evt_handle, %function
power_down_evt_handle:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldrb	r3, [r0]	@ zero_extendqisi2
	cmp	r3, #31
	ittt	eq
	ldreq	r3, .L3
	moveq	r2, #1
	strbeq	r2, [r3]
	bx	lr
.L4:
	.align	2
.L3:
	.word	.LANCHOR0
	.size	power_down_evt_handle, .-power_down_evt_handle
	.section	.text.provisionee_start,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	provisionee_start, %function
provisionee_start:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	ldr	r3, .L8
	ldrb	r3, [r3]	@ zero_extendqisi2
	push	{r4, lr}
	cbnz	r3, .L7
	ldr	r1, .L8+4
	ldr	r0, .L8+8
	bl	nrf_mesh_prov_generate_keys
	cbnz	r0, .L5
	ldr	r1, .L8+12
	mov	r2, r0
	pop	{r4, lr}
	ldr	r1, [r1, #20]
	ldr	r0, .L8+16
	movs	r3, #1
	b	nrf_mesh_prov_listen
.L7:
	movs	r0, #8
.L5:
	pop	{r4, pc}
.L9:
	.align	2
.L8:
	.word	.LANCHOR0
	.word	.LANCHOR1
	.word	.LANCHOR2
	.word	.LANCHOR3
	.word	.LANCHOR4
	.size	provisionee_start, .-provisionee_start
	.section	.text.prov_evt_handler,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	prov_evt_handler, %function
prov_evt_handler:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	ldrb	r3, [r0]	@ zero_extendqisi2
	subs	r3, r3, #2
	cmp	r3, #8
	bhi	.L10
	tbb	[pc, r3]
.L13:
	.byte	(.L17-.L13)/2
	.byte	(.L16-.L13)/2
	.byte	(.L15-.L13)/2
	.byte	(.L10-.L13)/2
	.byte	(.L10-.L13)/2
	.byte	(.L14-.L13)/2
	.byte	(.L10-.L13)/2
	.byte	(.L10-.L13)/2
	.byte	(.L12-.L13)/2
	.p2align 1
.L16:
	ldr	r3, .L45
	ldr	r3, [r3, #8]
	cbz	r3, .L10
	ldrb	r0, [r0, #8]	@ zero_extendqisi2
	cbz	r0, .L10
	ldr	r2, .L45+4
	movs	r1, #1
	pop	{r4, lr}
	strb	r1, [r2]
	bx	r3	@ indirect register sibling call
.L15:
	ldr	r3, .L45
	ldr	r3, [r3, #12]
	cbz	r3, .L10
	ldr	r2, .L45+4
	ldrb	r1, [r2]	@ zero_extendqisi2
	cbz	r1, .L10
	movs	r1, #0
	strb	r1, [r2]
.L44:
	pop	{r4, lr}
	bx	r3	@ indirect register sibling call
.L17:
	ldr	r3, .L45+8
	ldrb	r2, [r3]	@ zero_extendqisi2
	ldr	r3, .L45
	cbnz	r2, .L20
	ldr	r3, [r3, #16]
	cbz	r3, .L21
	ldr	r1, .L45+4
	strb	r2, [r1]
	blx	r3
.L21:
	pop	{r4, lr}
	b	provisionee_start
.L20:
	ldr	r3, [r3, #4]
	cmp	r3, #0
	bne	.L44
.L10:
	pop	{r4, pc}
.L14:
	ldr	r3, .L45
	ldr	r0, .L45+12
	ldr	r1, [r3, #24]
	movs	r2, #16
	bl	nrf_mesh_prov_auth_data_provide
	cmp	r0, #0
	beq	.L10
	pop	{r4, lr}
	b	app_error_handler_bare
.L12:
	ldrd	r1, r0, [r0, #8]
	bl	mesh_stack_provisioning_data_store
	cbz	r0, .L22
	bl	app_error_handler_bare
.L22:
	ldr	r3, .L45+8
	movs	r2, #1
	strb	r2, [r3]
	b	.L10
.L46:
	.align	2
.L45:
	.word	.LANCHOR3
	.word	.LANCHOR5
	.word	.LANCHOR6
	.word	.LANCHOR4
	.size	prov_evt_handler, .-prov_evt_handler
	.section	.text.mesh_provisionee_prov_start,"ax",%progbits
	.align	1
	.global	mesh_provisionee_prov_start
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_provisionee_prov_start, %function
mesh_provisionee_prov_start:
	@ args = 0, pretend = 0, frame = 16
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	ldr	r2, .L50
	ldr	r6, .L50+4
	ldr	r1, [r2, #4]	@ unaligned
	mov	r4, r0
	sub	sp, sp, #24
	ldr	r0, [r2]	@ unaligned
	add	r3, sp, #12
	stmia	r3!, {r0, r1}
	ldrh	r1, [r2, #8]	@ unaligned
	ldrb	r2, [r2, #10]	@ zero_extendqisi2
	strh	r1, [r3]	@ unaligned
	strb	r2, [r3, #2]
	ldmia	r4!, {r0, r1, r2, r3}
	mov	r5, r6
	stmia	r5!, {r0, r1, r2, r3}
	ldm	r4, {r0, r1, r2}
	stm	r5, {r0, r1, r2}
	ldr	r3, [r6, #24]
	cbz	r3, .L49
	ldr	r3, .L50+8
	str	r3, [sp]
	ldr	r2, .L50+12
	ldr	r1, .L50+16
	ldr	r0, .L50+20
	add	r3, sp, #12
	bl	nrf_mesh_prov_init
	cbnz	r0, .L47
	ldr	r0, .L50+24
	bl	nrf_mesh_prov_bearer_adv_interface_get
	mov	r1, r0
	ldr	r0, .L50+20
	bl	nrf_mesh_prov_bearer_add
	cbnz	r0, .L47
	ldr	r0, .L50+28
	bl	nrf_mesh_evt_handler_add
	bl	provisionee_start
.L47:
	add	sp, sp, #24
	@ sp needed
	pop	{r4, r5, r6, pc}
.L49:
	movs	r0, #7
	b	.L47
.L51:
	.align	2
.L50:
	.word	.LANCHOR7
	.word	.LANCHOR3
	.word	prov_evt_handler
	.word	.LANCHOR1
	.word	.LANCHOR2
	.word	.LANCHOR4
	.word	.LANCHOR8
	.word	.LANCHOR9
	.size	mesh_provisionee_prov_start, .-mesh_provisionee_prov_start
	.section	.text.mesh_provisionee_prov_listen_stop,"ax",%progbits
	.align	1
	.global	mesh_provisionee_prov_listen_stop
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_provisionee_prov_listen_stop, %function
mesh_provisionee_prov_listen_stop:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r0, .L53
	b	nrf_mesh_prov_listen_stop
.L54:
	.align	2
.L53:
	.word	.LANCHOR4
	.size	mesh_provisionee_prov_listen_stop, .-mesh_provisionee_prov_listen_stop
	.section .rodata
	.set	.LANCHOR7,. + 0
.LC0:
	.byte	1
	.2byte	1
	.byte	0
	.byte	1
	.byte	0
	.2byte	0
	.byte	0
	.2byte	0
	.section	.bss.m_device_identification_started,"aw",%nobits
	.set	.LANCHOR5,. + 0
	.type	m_device_identification_started, %object
	.size	m_device_identification_started, 1
m_device_identification_started:
	.space	1
	.section	.bss.m_device_provisioned,"aw",%nobits
	.set	.LANCHOR6,. + 0
	.type	m_device_provisioned, %object
	.size	m_device_provisioned, 1
m_device_provisioned:
	.space	1
	.section	.bss.m_is_in_power_down,"aw",%nobits
	.set	.LANCHOR0,. + 0
	.type	m_is_in_power_down, %object
	.size	m_is_in_power_down, 1
m_is_in_power_down:
	.space	1
	.section	.bss.m_params,"aw",%nobits
	.align	2
	.set	.LANCHOR3,. + 0
	.type	m_params, %object
	.size	m_params, 28
m_params:
	.space	28
	.section	.bss.m_private_key,"aw",%nobits
	.set	.LANCHOR1,. + 0
	.type	m_private_key, %object
	.size	m_private_key, 32
m_private_key:
	.space	32
	.section	.bss.m_prov_bearer_adv,"aw",%nobits
	.align	2
	.set	.LANCHOR8,. + 0
	.type	m_prov_bearer_adv, %object
	.size	m_prov_bearer_adv, 456
m_prov_bearer_adv:
	.space	456
	.section	.bss.m_prov_ctx,"aw",%nobits
	.align	2
	.set	.LANCHOR4,. + 0
	.type	m_prov_ctx, %object
	.size	m_prov_ctx, 308
m_prov_ctx:
	.space	308
	.section	.bss.m_public_key,"aw",%nobits
	.set	.LANCHOR2,. + 0
	.type	m_public_key, %object
	.size	m_public_key, 64
m_public_key:
	.space	64
	.section	.data.m_power_down_evt_handler,"aw"
	.align	2
	.set	.LANCHOR9,. + 0
	.type	m_power_down_evt_handler, %object
	.size	m_power_down_evt_handler, 12
m_power_down_evt_handler:
	.word	power_down_evt_handle
	.space	8
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
