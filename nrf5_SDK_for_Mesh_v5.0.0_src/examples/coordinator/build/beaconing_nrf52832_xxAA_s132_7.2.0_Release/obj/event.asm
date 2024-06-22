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
	.file	"event.c"
	.text
	.section	.text.event_handle,"ax",%progbits
	.align	1
	.global	event_handle
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	event_handle, %function
event_handle:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, r6, r7, lr}
	mov	r5, r0
	cbnz	r0, .L2
	.syntax unified
@ 73 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\event.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L2:
	ldr	r7, .L18
	ldr	r4, [r7]
	cbz	r4, .L1
	ldr	r6, .L18+4
	movs	r3, #1
	strb	r3, [r6]
.L5:
	ldrb	r3, [r4, #4]	@ zero_extendqisi2
	cbnz	r3, .L4
	ldr	r3, [r4, #-4]
	mov	r0, r5
	blx	r3
.L4:
	ldr	r4, [r4]
	cmp	r4, #0
	bne	.L5
	ldrb	r3, [r6]	@ zero_extendqisi2
	cmp	r3, #2
	beq	.L6
.L10:
	movs	r3, #0
	strb	r3, [r6]
.L1:
	pop	{r3, r4, r5, r6, r7, pc}
.L6:
	ldr	r1, [r7]
	ldr	r4, .L18
.L7:
	cmp	r1, #0
	beq	.L10
	ldrb	r3, [r1, #4]	@ zero_extendqisi2
	ldr	r5, [r1]
	cbz	r3, .L8
	mov	r0, r4
	bl	list_remove
.L8:
	mov	r1, r5
	b	.L7
.L19:
	.align	2
.L18:
	.word	.LANCHOR0
	.word	.LANCHOR1
	.size	event_handle, .-event_handle
	.section	.text.event_handler_add,"ax",%progbits
	.align	1
	.global	event_handler_add
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	event_handler_add, %function
event_handler_add:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	mov	r4, r0
	cbnz	r0, .L21
	.syntax unified
@ 100 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\event.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L21:
	movs	r3, #0
	strb	r3, [r4, #8]
	adds	r1, r4, #4
	ldr	r0, .L22
	pop	{r4, lr}
	b	list_add
.L23:
	.align	2
.L22:
	.word	.LANCHOR0
	.size	event_handler_add, .-event_handler_add
	.section	.text.event_handler_remove,"ax",%progbits
	.align	1
	.global	event_handler_remove
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	event_handler_remove, %function
event_handler_remove:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	mov	r4, r0
	cbnz	r0, .L25
	.syntax unified
@ 107 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\event.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L25:
	ldr	r2, .L29
	ldrb	r3, [r2]	@ zero_extendqisi2
	subs	r3, r3, #1
	cmp	r3, #1
	bhi	.L26
	movs	r3, #2
	strb	r3, [r2]
	movs	r3, #1
	strb	r3, [r4, #8]
	pop	{r4, pc}
.L26:
	adds	r1, r4, #4
	ldr	r0, .L29+4
	pop	{r4, lr}
	b	list_remove
.L30:
	.align	2
.L29:
	.word	.LANCHOR1
	.word	.LANCHOR0
	.size	event_handler_remove, .-event_handler_remove
	.section	.bss.m_event_handler_state,"aw",%nobits
	.set	.LANCHOR1,. + 0
	.type	m_event_handler_state, %object
	.size	m_event_handler_state, 1
m_event_handler_state:
	.space	1
	.section	.bss.mp_evt_handlers_head,"aw",%nobits
	.align	2
	.set	.LANCHOR0,. + 0
	.type	mp_evt_handlers_head, %object
	.size	mp_evt_handlers_head, 4
mp_evt_handlers_head:
	.space	4
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
