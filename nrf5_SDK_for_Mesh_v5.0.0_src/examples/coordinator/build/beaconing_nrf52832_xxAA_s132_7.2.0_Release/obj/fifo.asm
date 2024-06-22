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
	.file	"fifo.c"
	.text
	.section	.text.fifo_init,"ax",%progbits
	.align	1
	.global	fifo_init
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_init, %function
fifo_init:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	mov	r4, r0
	cbnz	r0, .L2
	.syntax unified
@ 56 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L2:
	ldr	r3, [r4, #4]
	cbz	r3, .L3
	ldr	r3, [r4]
	cbz	r3, .L3
	ldr	r3, [r4, #8]
	cbnz	r3, .L4
.L3:
	.syntax unified
@ 57 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L4:
	ldr	r3, [r4, #8]
	subs	r2, r3, #1
	tst	r2, r3
	beq	.L5
	.syntax unified
@ 58 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L5:
	movs	r3, #0
	strd	r3, r3, [r4, #12]
	pop	{r4, pc}
	.size	fifo_init, .-fifo_init
	.section	.text.fifo_push,"ax",%progbits
	.align	1
	.global	fifo_push
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_push, %function
fifo_push:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, lr}
	mov	r4, r0
	cbz	r0, .L19
	cbz	r1, .L19
	ldr	r3, [r0, #8]
	cbz	r3, .L20
	.syntax unified
@ 82 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	MRS r5, primask
@ 0 "" 2
@ 82 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrd	r0, r2, [r0, #8]
	ldr	r3, [r4, #16]
	add	r3, r3, r0
	cmp	r3, r2
	bne	.L17
	cbnz	r5, .L21
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L21:
	movs	r5, #4
	b	.L15
.L17:
	subs	r0, r0, #1
	ands	r0, r0, r2
	ldrd	r3, r2, [r4]
	mla	r0, r2, r0, r3
	bl	memcpy
	ldr	r3, [r4, #12]
	adds	r3, r3, #1
	str	r3, [r4, #12]
	cbnz	r5, .L22
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L15:
	mov	r0, r5
	pop	{r3, r4, r5, pc}
.L19:
	movs	r5, #14
	b	.L15
.L20:
	movs	r5, #9
	b	.L15
.L22:
	movs	r5, #0
	b	.L15
	.size	fifo_push, .-fifo_push
	.section	.text.fifo_pop,"ax",%progbits
	.align	1
	.global	fifo_pop
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_pop, %function
fifo_pop:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	mov	r6, r1
	mov	r4, r0
	cbz	r0, .L27
	ldr	r3, [r0, #8]
	cbz	r3, .L28
	.syntax unified
@ 123 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	MRS r5, primask
@ 0 "" 2
@ 123 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrd	r3, r1, [r0, #12]
	cmp	r1, r3
	bne	.L25
	cbnz	r5, .L29
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L29:
	movs	r5, #5
	b	.L23
.L25:
	cbz	r6, .L26
	ldr	r3, [r0, #8]
	subs	r3, r3, #1
	ands	r3, r3, r1
	ldrd	r1, r2, [r0]
	mov	r0, r6
	mla	r1, r2, r3, r1
	bl	memcpy
.L26:
	ldr	r3, [r4, #16]
	adds	r3, r3, #1
	str	r3, [r4, #16]
	cbnz	r5, .L30
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L23:
	mov	r0, r5
	pop	{r4, r5, r6, pc}
.L27:
	movs	r5, #14
	b	.L23
.L28:
	movs	r5, #9
	b	.L23
.L30:
	movs	r5, #0
	b	.L23
	.size	fifo_pop, .-fifo_pop
	.section	.text.fifo_peek_at,"ax",%progbits
	.align	1
	.global	fifo_peek_at
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_peek_at, %function
fifo_peek_at:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	mov	r3, r2
	mov	r6, r1
	cbz	r0, .L38
	cbz	r1, .L38
	ldr	r2, [r0, #8]
	cbz	r2, .L39
	.syntax unified
@ 156 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	MRS r4, primask
@ 0 "" 2
@ 156 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\fifo.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrd	r5, r1, [r0, #12]
	subs	r5, r5, r1
	cmp	r3, r5
	bcc	.L36
	cbnz	r4, .L40
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L40:
	movs	r4, #5
	b	.L34
.L36:
	ldrd	r2, r5, [r0, #4]
	add	r3, r3, r1
	subs	r5, r5, #1
	ldr	r1, [r0]
	ands	r3, r3, r5
	mla	r1, r2, r3, r1
	mov	r0, r6
	bl	memcpy
	cbnz	r4, .L41
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L34:
	mov	r0, r4
	pop	{r4, r5, r6, pc}
.L38:
	movs	r4, #14
	b	.L34
.L39:
	movs	r4, #9
	b	.L34
.L41:
	movs	r4, #0
	b	.L34
	.size	fifo_peek_at, .-fifo_peek_at
	.section	.text.fifo_peek,"ax",%progbits
	.align	1
	.global	fifo_peek
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_peek, %function
fifo_peek:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	movs	r2, #0
	b	fifo_peek_at
	.size	fifo_peek, .-fifo_peek
	.section	.text.fifo_flush,"ax",%progbits
	.align	1
	.global	fifo_flush
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_flush, %function
fifo_flush:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r3, [r0, #12]
	str	r3, [r0, #16]
	bx	lr
	.size	fifo_flush, .-fifo_flush
	.section	.text.fifo_get_len,"ax",%progbits
	.align	1
	.global	fifo_get_len
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_get_len, %function
fifo_get_len:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldrd	r2, r0, [r0, #12]
	subs	r0, r2, r0
	bx	lr
	.size	fifo_get_len, .-fifo_get_len
	.section	.text.fifo_is_full,"ax",%progbits
	.align	1
	.global	fifo_is_full
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_is_full, %function
fifo_is_full:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r3, [r0, #16]
	ldr	r2, [r0, #8]
	ldr	r0, [r0, #12]
	add	r3, r3, r2
	subs	r3, r3, r0
	rsbs	r0, r3, #0
	adcs	r0, r0, r3
	bx	lr
	.size	fifo_is_full, .-fifo_is_full
	.section	.text.fifo_is_empty,"ax",%progbits
	.align	1
	.global	fifo_is_empty
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	fifo_is_empty, %function
fifo_is_empty:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldrd	r0, r2, [r0, #12]
	subs	r3, r2, r0
	rsbs	r0, r3, #0
	adcs	r0, r0, r3
	bx	lr
	.size	fifo_is_empty, .-fifo_is_empty
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
