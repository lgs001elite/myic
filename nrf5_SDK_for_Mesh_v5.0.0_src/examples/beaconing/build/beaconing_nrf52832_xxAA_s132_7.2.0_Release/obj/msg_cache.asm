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
	.file	"msg_cache.c"
	.text
	.section	.text.msg_cache_init,"ax",%progbits
	.align	1
	.global	msg_cache_init
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	msg_cache_init, %function
msg_cache_init:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	movs	r2, #0
	ldr	r1, .L4
	mov	r3, r2
.L2:
	adds	r2, r2, #1
	cmp	r2, #32
	strh	r3, [r1, #2]	@ movhi
	str	r3, [r1, #4]
	strb	r3, [r1], #8
	bne	.L2
	ldr	r2, .L4+4
	str	r3, [r2]
	bx	lr
.L5:
	.align	2
.L4:
	.word	.LANCHOR0
	.word	.LANCHOR1
	.size	msg_cache_init, .-msg_cache_init
	.section	.text.msg_cache_entry_exists,"ax",%progbits
	.align	1
	.global	msg_cache_entry_exists
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	msg_cache_entry_exists, %function
msg_cache_entry_exists:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	ldr	r3, .L16
	push	{r4, r5, r6, r7, lr}
	ldr	r3, [r3]
	ldr	r5, .L16+4
	mov	r4, r0
	movs	r2, #32
.L10:
	cbz	r3, .L11
	subs	r3, r3, #1
.L7:
	ldrb	r0, [r5, r3, lsl #3]	@ zero_extendqisi2
	cbz	r0, .L8
	add	r6, r5, r3, lsl #3
	ldrh	r7, [r6, #2]
	cmp	r7, r4
	bne	.L9
	ldr	r6, [r6, #4]
	cmp	r6, r1
	beq	.L8
.L9:
	subs	r2, r2, #1
	bne	.L10
	mov	r0, r2
.L8:
	pop	{r4, r5, r6, r7, pc}
.L11:
	movs	r3, #31
	b	.L7
.L17:
	.align	2
.L16:
	.word	.LANCHOR1
	.word	.LANCHOR0
	.size	msg_cache_entry_exists, .-msg_cache_entry_exists
	.section	.text.msg_cache_entry_add,"ax",%progbits
	.align	1
	.global	msg_cache_entry_add
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	msg_cache_entry_add, %function
msg_cache_entry_add:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	ldr	r2, .L21
	push	{r4, r5, lr}
	ldr	r3, [r2]
	ldr	r4, .L21+4
	add	r5, r4, r3, lsl #3
	cmp	r3, #31
	str	r1, [r5, #4]
	mov	r1, #1
	strb	r1, [r4, r3, lsl #3]
	add	r1, r3, r1
	it	eq
	moveq	r3, #0
	strh	r0, [r5, #2]	@ movhi
	ite	ne
	strne	r1, [r2]
	streq	r3, [r2]
	pop	{r4, r5, pc}
.L22:
	.align	2
.L21:
	.word	.LANCHOR1
	.word	.LANCHOR0
	.size	msg_cache_entry_add, .-msg_cache_entry_add
	.section	.text.msg_cache_clear,"ax",%progbits
	.align	1
	.global	msg_cache_clear
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	msg_cache_clear, %function
msg_cache_clear:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	movs	r3, #0
	ldr	r2, .L26
	mov	r1, r3
.L24:
	strb	r1, [r2, r3, lsl #3]
	adds	r3, r3, #1
	cmp	r3, #32
	bne	.L24
	bx	lr
.L27:
	.align	2
.L26:
	.word	.LANCHOR0
	.size	msg_cache_clear, .-msg_cache_clear
	.section	.bss.m_msg_cache,"aw",%nobits
	.align	2
	.set	.LANCHOR0,. + 0
	.type	m_msg_cache, %object
	.size	m_msg_cache, 256
m_msg_cache:
	.space	256
	.section	.bss.m_msg_cache_head,"aw",%nobits
	.align	2
	.set	.LANCHOR1,. + 0
	.type	m_msg_cache_head, %object
	.size	m_msg_cache_head, 4
m_msg_cache_head:
	.space	4
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
