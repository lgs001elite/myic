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
	.file	"packet_buffer.c"
	.text
	.section	.text.m_index_increment,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	m_index_increment, %function
m_index_increment:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldrh	r3, [r1]
	ldr	r2, [r0, #8]
	ldrh	r2, [r2, r3]
	adds	r2, r2, #7
	bic	r2, r2, #3
	add	r3, r3, r2
	ldrh	r2, [r0]
	uxth	r3, r3
	subs	r2, r2, #4
	cmp	r3, r2
	it	hi
	movhi	r3, #0
	strh	r3, [r1]	@ movhi
	bx	lr
	.size	m_index_increment, .-m_index_increment
	.section	.text.m_get_next_packet,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	m_get_next_packet, %function
m_get_next_packet:
	@ args = 0, pretend = 0, frame = 8
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r4, lr}
	ldr	r3, [r0, #8]
	subs	r1, r1, r3
	strh	r1, [sp, #6]	@ movhi
	add	r1, sp, #6
	bl	m_index_increment
	ldrh	r3, [sp, #6]
	ldr	r0, [r0, #8]
	add	r0, r0, r3
	add	sp, sp, #8
	@ sp needed
	pop	{r4, pc}
	.size	m_get_next_packet, .-m_get_next_packet
	.section	.text.packet_buffer_max_packet_len_get,"ax",%progbits
	.align	1
	.global	packet_buffer_max_packet_len_get
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_max_packet_len_get, %function
packet_buffer_max_packet_len_get:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	mov	r4, r0
	cbnz	r0, .L5
	.syntax unified
@ 193 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L5:
	ldrh	r3, [r4]
	cmp	r3, #4
	bhi	.L6
	.syntax unified
@ 194 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L6:
	ldrh	r0, [r4]
	subs	r0, r0, #4
	uxth	r0, r0
	pop	{r4, pc}
	.size	packet_buffer_max_packet_len_get, .-packet_buffer_max_packet_len_get
	.section	.text.packet_buffer_init,"ax",%progbits
	.align	1
	.global	packet_buffer_init
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_init, %function
packet_buffer_init:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	mov	r6, r0
	mov	r5, r2
	mov	r4, r1
	cbnz	r1, .L8
	.syntax unified
@ 202 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L8:
	cbnz	r6, .L9
	.syntax unified
@ 203 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L9:
	cmp	r4, #536870912
	bls	.L10
	mov	r3, #268435456
	ldr	r3, [r3, #268]
	add	r3, r3, #524288
	cmp	r4, r3, lsl #10
	bcs	.L11
.L12:
	subs	r3, r5, #1
	add	r3, r3, r4
	cmp	r3, #536870912
	bls	.L14
	mov	r2, #268435456
	ldr	r2, [r2, #268]
	add	r2, r2, #524288
	cmp	r3, r2, lsl #10
	bcs	.L15
.L16:
	cmp	r5, #4
	bhi	.L18
	.syntax unified
@ 206 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L18:
	movs	r3, #0
	strh	r5, [r6]	@ movhi
	strh	r3, [r6, #2]	@ movhi
	strh	r3, [r6, #4]	@ movhi
	str	r4, [r6, #8]
	subs	r5, r5, #4
	strb	r3, [r4, #2]
	strh	r5, [r4]	@ movhi
	pop	{r4, r5, r6, pc}
.L10:
	cmp	r4, #8388608
	bls	.L13
.L11:
	mov	r3, #268435456
	ldr	r3, [r3, #268]
	add	r3, r3, #8192
	cmp	r4, r3, lsl #10
	bcc	.L12
.L13:
	.syntax unified
@ 204 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
	b	.L12
.L14:
	cmp	r3, #8388608
	bls	.L17
.L15:
	mov	r2, #268435456
	ldr	r2, [r2, #268]
	add	r2, r2, #8192
	cmp	r3, r2, lsl #10
	bcc	.L16
.L17:
	.syntax unified
@ 205 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
	b	.L16
	.size	packet_buffer_init, .-packet_buffer_init
	.section	.text.packet_buffer_flush,"ax",%progbits
	.align	1
	.global	packet_buffer_flush
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_flush, %function
packet_buffer_flush:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, lr}
	mov	r4, r0
	cbnz	r0, .L20
	.syntax unified
@ 219 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L20:
	ldrh	r2, [r4, #2]
	ldr	r3, [r4, #8]
	add	r3, r3, r2
	ldrb	r3, [r3, #2]	@ zero_extendqisi2
	cmp	r3, #1
	bne	.L21
	.syntax unified
@ 221 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L21:
	.syntax unified
@ 225 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r5, primask
@ 0 "" 2
@ 225 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldr	r2, [r4, #8]
	ldrh	r1, [r4, #4]
	add	r1, r1, r2
	ldrb	r3, [r1, #2]	@ zero_extendqisi2
	cmp	r3, #3
	bne	.L22
	mov	r0, r4
	bl	m_get_next_packet
	ldr	r3, [r4, #8]
	subs	r3, r0, r3
	strh	r3, [r4, #2]	@ movhi
	movs	r3, #0
	strb	r3, [r0, #2]
.L23:
	cbnz	r5, .L19
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L19:
	pop	{r3, r4, r5, pc}
.L22:
	movs	r3, #0
	strb	r3, [r2, #2]
	strh	r3, [r4, #2]	@ movhi
	strh	r3, [r4, #4]	@ movhi
	b	.L23
	.size	packet_buffer_flush, .-packet_buffer_flush
	.section	.text.packet_buffer_reserve,"ax",%progbits
	.align	1
	.global	packet_buffer_reserve
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_reserve, %function
packet_buffer_reserve:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, r6, r7, lr}
	mov	r6, r1
	mov	r5, r2
	mov	r4, r0
	cbnz	r0, .L26
	.syntax unified
@ 247 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L26:
	cbnz	r6, .L27
	.syntax unified
@ 248 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L27:
	ldrh	r2, [r4, #2]
	ldr	r3, [r4, #8]
	add	r3, r3, r2
	ldrb	r3, [r3, #2]	@ zero_extendqisi2
	cmp	r3, #1
	bne	.L28
	.syntax unified
@ 249 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L28:
	cmp	r5, #0
	beq	.L36
	ldrh	r3, [r4]
	subs	r3, r3, #4
	uxth	r3, r3
	cmp	r5, r3
	bhi	.L36
	.syntax unified
@ 258 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r7, primask
@ 0 "" 2
@ 258 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrh	r2, [r4, #2]
	ldrh	r3, [r4, #4]
	adds	r0, r5, #7
	bic	r0, r0, #3
	cmp	r2, r3
	uxth	r0, r0
	bcs	.L30
	subs	r3, r3, r2
	cmp	r0, r3
	ble	.L31
.L38:
	movs	r0, #4
	b	.L32
.L30:
	bls	.L33
	ldrh	r1, [r4]
	subs	r1, r1, r2
	cmp	r1, r0
	bcs	.L31
	cmp	r0, r3
	bhi	.L38
	cmp	r1, #3
	itttt	hi
	ldrhi	r3, [r4, #8]
	addhi	r3, r3, r2
	movhi	r2, #4
	strbhi	r2, [r3, #2]
	movs	r3, #0
	strh	r3, [r4, #2]	@ movhi
.L31:
	ldrh	r2, [r4, #2]
	ldr	r1, [r4, #8]
	adds	r3, r1, r2
	strh	r5, [r1, r2]	@ movhi
	movs	r2, #1
	strb	r2, [r3, #2]
	movs	r0, #0
	str	r3, [r6]
.L32:
	cbnz	r7, .L25
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L25:
	pop	{r3, r4, r5, r6, r7, pc}
.L33:
	ldr	r2, [r4, #8]
	add	r3, r3, r2
	ldrb	r3, [r3, #2]	@ zero_extendqisi2
	cmp	r3, #0
	bne	.L38
	strb	r3, [r2, #2]
	strh	r3, [r4, #2]	@ movhi
	strh	r3, [r4, #4]	@ movhi
	b	.L31
.L36:
	movs	r0, #9
	b	.L25
	.size	packet_buffer_reserve, .-packet_buffer_reserve
	.section	.text.packet_buffer_commit,"ax",%progbits
	.align	1
	.global	packet_buffer_commit
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_commit, %function
packet_buffer_commit:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, r6, r7, lr}
	mov	r5, r1
	mov	r6, r2
	mov	r4, r0
	cbnz	r0, .L40
	.syntax unified
@ 273 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L40:
	cbnz	r5, .L41
	.syntax unified
@ 274 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L41:
	ldrb	r3, [r5, #2]	@ zero_extendqisi2
	cmp	r3, #1
	beq	.L42
	.syntax unified
@ 275 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L42:
	ldrh	r3, [r5]
	cmp	r3, r6
	bcs	.L43
	.syntax unified
@ 276 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L43:
	cbnz	r6, .L44
	.syntax unified
@ 277 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L44:
	.syntax unified
@ 282 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r7, primask
@ 0 "" 2
@ 282 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	movs	r3, #2
	strb	r3, [r5, #2]
	adds	r1, r4, r3
	strh	r6, [r5]	@ movhi
	mov	r0, r4
	bl	m_index_increment
	ldrh	r2, [r4, #2]
	ldrh	r3, [r4, #4]
	cmp	r3, r2
	itttt	ne
	ldrne	r3, [r4, #8]
	addne	r3, r3, r2
	movne	r2, #0
	strbne	r2, [r3, #2]
	cbnz	r7, .L39
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L39:
	pop	{r3, r4, r5, r6, r7, pc}
	.size	packet_buffer_commit, .-packet_buffer_commit
	.section	.text.packet_buffer_pop,"ax",%progbits
	.align	1
	.global	packet_buffer_pop
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_pop, %function
packet_buffer_pop:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	mov	r5, r1
	mov	r4, r0
	cbnz	r0, .L51
	.syntax unified
@ 307 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L51:
	cbnz	r5, .L52
	.syntax unified
@ 309 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L52:
	.syntax unified
@ 315 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r6, primask
@ 0 "" 2
@ 315 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrh	r2, [r4, #4]
	ldr	r3, [r4, #8]
	add	r3, r3, r2
	ldrb	r2, [r3, #2]	@ zero_extendqisi2
	cmp	r2, #4
	bne	.L53
	adds	r1, r4, #4
	mov	r0, r4
	bl	m_index_increment
	ldrh	r2, [r4, #4]
	ldr	r3, [r4, #8]
	add	r3, r3, r2
.L53:
	ldrb	r2, [r3, #2]	@ zero_extendqisi2
	cmp	r2, #2
	beq	.L54
	cmp	r2, #3
	beq	.L55
	movs	r0, #5
.L56:
	cbnz	r6, .L50
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L50:
	pop	{r4, r5, r6, pc}
.L54:
	movs	r2, #3
	strb	r2, [r3, #2]
	str	r3, [r5]
.L58:
	movs	r0, #0
	b	.L56
.L55:
	.syntax unified
@ 332 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
	b	.L58
	.size	packet_buffer_pop, .-packet_buffer_pop
	.section	.text.packet_buffer_can_pop,"ax",%progbits
	.align	1
	.global	packet_buffer_can_pop
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_can_pop, %function
packet_buffer_can_pop:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, lr}
	mov	r4, r0
	cbnz	r0, .L60
	.syntax unified
@ 345 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L60:
	.syntax unified
@ 348 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r5, primask
@ 0 "" 2
@ 348 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrh	r0, [r4, #4]
	ldr	r1, [r4, #8]
	add	r1, r1, r0
	ldrb	r3, [r1, #2]	@ zero_extendqisi2
	cmp	r3, #4
	bne	.L61
	mov	r0, r4
	bl	m_get_next_packet
	mov	r1, r0
.L61:
	ldrb	r0, [r1, #2]	@ zero_extendqisi2
	subs	r3, r0, #2
	rsbs	r0, r3, #0
	adcs	r0, r0, r3
	cbnz	r5, .L62
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L62:
	pop	{r3, r4, r5, pc}
	.size	packet_buffer_can_pop, .-packet_buffer_can_pop
	.section	.text.packet_buffer_packets_ready_to_pop,"ax",%progbits
	.align	1
	.global	packet_buffer_packets_ready_to_pop
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_packets_ready_to_pop, %function
packet_buffer_packets_ready_to_pop:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, lr}
	mov	r4, r0
	cbnz	r0, .L64
	.syntax unified
@ 363 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L64:
	.syntax unified
@ 366 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r5, primask
@ 0 "" 2
@ 366 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrh	r0, [r4, #4]
	ldr	r1, [r4, #8]
	add	r1, r1, r0
.L65:
	ldrb	r0, [r1, #2]	@ zero_extendqisi2
	subs	r3, r0, #3
	cmp	r3, #1
	bls	.L66
	subs	r3, r0, #2
	rsbs	r0, r3, #0
	adcs	r0, r0, r3
	cbnz	r5, .L67
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L67:
	pop	{r3, r4, r5, pc}
.L66:
	mov	r0, r4
	bl	m_get_next_packet
	mov	r1, r0
	b	.L65
	.size	packet_buffer_packets_ready_to_pop, .-packet_buffer_packets_ready_to_pop
	.section	.text.packet_buffer_free,"ax",%progbits
	.align	1
	.global	packet_buffer_free
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_free, %function
packet_buffer_free:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, r6, r7, lr}
	mov	r5, r1
	mov	r4, r0
	cbnz	r0, .L69
	.syntax unified
@ 383 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L69:
	cbnz	r5, .L70
	.syntax unified
@ 384 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L70:
	.syntax unified
@ 387 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r6, primask
@ 0 "" 2
@ 387 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrb	r3, [r5, #2]	@ zero_extendqisi2
	cmp	r3, #1
	beq	.L71
	cmp	r3, #3
	bne	.L72
	ldrh	r2, [r4, #4]
	ldr	r3, [r4, #8]
	add	r3, r3, r2
	cmp	r5, r3
	beq	.L73
	.syntax unified
@ 86 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L73:
	movs	r7, #0
	strb	r7, [r5, #2]
	adds	r1, r4, #4
	mov	r0, r4
	bl	m_index_increment
	ldrh	r2, [r4, #4]
	ldr	r3, [r4, #8]
	add	r3, r3, r2
	ldrb	r3, [r3, #2]	@ zero_extendqisi2
	cmp	r3, #4
	bne	.L74
	strh	r7, [r4, #4]	@ movhi
.L74:
	cbnz	r6, .L68
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L68:
	pop	{r3, r4, r5, r6, r7, pc}
.L71:
	ldrh	r2, [r4, #2]
	ldr	r3, [r4, #8]
	add	r3, r3, r2
	cmp	r5, r3
	beq	.L75
	.syntax unified
@ 100 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L75:
	movs	r3, #0
	strb	r3, [r5, #2]
	b	.L74
.L72:
	.syntax unified
@ 399 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
	b	.L74
	.size	packet_buffer_free, .-packet_buffer_free
	.section	.text.packet_buffer_is_empty,"ax",%progbits
	.align	1
	.global	packet_buffer_is_empty
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	packet_buffer_is_empty, %function
packet_buffer_is_empty:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	.syntax unified
@ 411 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	MRS r4, primask
@ 0 "" 2
@ 411 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\packet_buffer.c" 1
	cpsid i
@ 0 "" 2
	.thumb
	.syntax unified
	ldrh	r2, [r0, #4]
	ldr	r1, [r0, #8]
	add	r1, r1, r2
	ldrb	r3, [r1, #2]	@ zero_extendqisi2
	cmp	r3, #4
	bne	.L78
	bl	m_get_next_packet
	mov	r1, r0
.L78:
	ldrb	r0, [r1, #2]	@ zero_extendqisi2
	clz	r0, r0
	lsrs	r0, r0, #5
	cbnz	r4, .L79
	.syntax unified
@ 198 "../../../nRF5_SDK_17.0.2_d674dde/components/toolchain/cmsis/include/cmsis_gcc.h" 1
	cpsie i
@ 0 "" 2
	.thumb
	.syntax unified
.L79:
	pop	{r4, pc}
	.size	packet_buffer_is_empty, .-packet_buffer_is_empty
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
