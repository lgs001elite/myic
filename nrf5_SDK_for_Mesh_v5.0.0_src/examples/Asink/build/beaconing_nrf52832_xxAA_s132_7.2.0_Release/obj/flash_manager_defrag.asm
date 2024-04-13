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
	.file	"flash_manager_defrag.c"
	.text
	.section	.text.get_last_page,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	get_last_page, %function
get_last_page:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldrb	r3, [r0, #4]	@ zero_extendqisi2
	ldrb	r2, [r0, #5]	@ zero_extendqisi2
	subs	r3, r3, r2
	add	r3, r3, #1044480
	addw	r3, r3, #4095
	add	r0, r0, r3, lsl #12
	bx	lr
	.size	get_last_page, .-get_last_page
	.section	.text.freezing,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	freezing, %function
freezing:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r3, .L3
	movs	r2, #0
	strb	r2, [r3, #24]
	str	r2, [r3, #8]
	movs	r0, #2
	bx	lr
.L4:
	.align	2
.L3:
	.word	.LANCHOR0
	.size	freezing, .-freezing
	.section	.text.defrag_on_end,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	defrag_on_end, %function
defrag_on_end:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	ldr	r0, .L6
	ldr	r4, [r0, #8]
	movs	r2, #28
	movs	r1, #0
	bl	memset
	mov	r0, r4
	pop	{r4, lr}
	b	flash_manager_on_defrag_end
.L7:
	.align	2
.L6:
	.word	.LANCHOR0
	.size	defrag_on_end, .-defrag_on_end
	.section	.text.execute_procedure_step,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	execute_procedure_step, %function
execute_procedure_step:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	ldr	r4, .L23
	ldr	r3, [r4, #12]
	cbnz	r3, .L9
	.syntax unified
@ 518 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L9:
	ldrb	r3, [r4, #24]	@ zero_extendqisi2
	cbz	r3, .L10
	.syntax unified
@ 519 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L10:
	ldr	r3, [r4, #4]
	cmp	r3, #10
	bls	.L11
	.syntax unified
@ 520 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L11:
	ldr	r5, .L23+4
	movs	r6, #0
.L17:
	ldr	r3, [r4, #4]
	ldr	r3, [r5, r3, lsl #2]
	blx	r3
	cmp	r0, #2
	beq	.L12
	cmp	r0, #3
	beq	.L13
	cmp	r0, #1
	bne	.L8
	ldr	r3, [r4, #4]
	adds	r3, r3, #1
	cmp	r3, #10
	str	r3, [r4, #4]
	bls	.L15
	.syntax unified
@ 532 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L15:
	ldrb	r3, [r4, #24]	@ zero_extendqisi2
	cmp	r3, #0
	beq	.L17
	b	.L8
.L13:
	str	r6, [r4, #4]
	b	.L15
.L12:
	ldrb	r3, [r4, #24]	@ zero_extendqisi2
	cbz	r3, .L16
	strb	r0, [r4]
.L8:
	pop	{r4, r5, r6, pc}
.L16:
	pop	{r4, r5, r6, lr}
	b	defrag_on_end
.L24:
	.align	2
.L23:
	.word	.LANCHOR0
	.word	.LANCHOR1
	.size	execute_procedure_step, .-execute_procedure_step
	.section	.text.jump_to_step,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	jump_to_step, %function
jump_to_step:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r2, .L31
	movs	r3, #0
.L28:
	ldr	r1, [r2], #4
	cmp	r1, r0
	bne	.L26
	ldr	r2, .L31+4
	str	r3, [r2, #4]
	bx	lr
.L26:
	adds	r3, r3, #1
	cmp	r3, #11
	bne	.L28
	.syntax unified
@ 512 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	b	mesh_assertion_handler
.L32:
	.align	2
.L31:
	.word	.LANCHOR1
	.word	.LANCHOR0
	.size	jump_to_step, .-jump_to_step
	.section	.text.get_next_entry,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	get_next_entry, %function
get_next_entry:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	ldrh	r3, [r0]
	push	{r4, lr}
	mov	r4, r0
	cbnz	r3, .L34
	.syntax unified
@ 133 "../../mesh/core/include/flash_manager_internal.h" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L34:
	ldrh	r0, [r4]
	ldr	r3, .L37
	add	r0, r4, r0, lsl #2
	bics	r2, r0, r3
	beq	.L35
	ldrh	r2, [r4, #2]
	cmp	r2, #32512
	bne	.L33
.L35:
	and	r0, r4, r3
	add	r0, r0, #4096
	ldrb	r3, [r0]	@ zero_extendqisi2
	add	r0, r0, r3
.L33:
	pop	{r4, pc}
.L38:
	.align	2
.L37:
	.word	-4096
	.size	get_next_entry, .-get_next_entry
	.section	.text.get_next_data_entry,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	get_next_data_entry, %function
get_next_data_entry:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	mov	r4, r0
	mov	r5, r1
	movw	r6, #32510
.L41:
	bl	get_next_entry
	cmp	r0, r5
	bcs	.L43
	cmp	r4, r0
	bcs	.L43
	ldrh	r3, [r0, #2]
	subs	r3, r3, #1
	uxth	r3, r3
	cmp	r3, r6
	bhi	.L41
.L39:
	pop	{r4, r5, r6, pc}
.L43:
	movs	r0, #0
	b	.L39
	.size	get_next_data_entry, .-get_next_data_entry
	.section	.text.on_flash_op_end,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	on_flash_op_end, %function
on_flash_op_end:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldrb	r2, [r1]	@ zero_extendqisi2
	ldr	r3, .L49
	cmp	r2, #3
	itt	eq
	moveq	r1, #0
	strbeq	r1, [r3, #24]
	ldrb	r1, [r3]	@ zero_extendqisi2
	cmp	r1, #1
	bne	.L47
	ldrb	r3, [r3, #24]	@ zero_extendqisi2
	cbnz	r3, .L45
	b	execute_procedure_step
.L47:
	cmp	r1, #2
	bne	.L45
	cmp	r2, #3
	bne	.L45
	b	defrag_on_end
.L45:
	bx	lr
.L50:
	.align	2
.L49:
	.word	.LANCHOR0
	.size	on_flash_op_end, .-on_flash_op_end
	.section	.text.check_for_invalid_entries,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	check_for_invalid_entries, %function
check_for_invalid_entries:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	ldr	r4, .L55
	ldr	r3, [r4, #12]
	ldrb	r0, [r3]	@ zero_extendqisi2
	movs	r2, #0
	add	r1, r3, #4096
	add	r0, r0, r3
	bl	entry_get
	cbnz	r0, .L53
	ldr	r1, [r4, #12]
	mov	r0, r1
	bl	get_last_page
	cmp	r1, r0
	beq	.L54
	add	r1, r1, #4096
	str	r1, [r4, #12]
	movs	r0, #3
.L52:
	pop	{r4, pc}
.L53:
	movs	r0, #1
	b	.L52
.L54:
	movs	r0, #2
	b	.L52
.L56:
	.align	2
.L55:
	.word	.LANCHOR0
	.size	check_for_invalid_entries, .-check_for_invalid_entries
	.section	.text.erase_source,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	erase_source, %function
erase_source:
	@ args = 0, pretend = 0, frame = 16
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, r3, r4, lr}
	ldr	r3, .L58
	movs	r2, #2
	ldr	r3, [r3, #12]
	strb	r2, [sp]
	str	r3, [sp, #4]
	ldr	r2, .L58+4
	mov	r3, #4096
	mov	r1, sp
	movs	r0, #1
	str	r3, [sp, #8]
	bl	mesh_flash_op_push
	clz	r0, r0
	lsrs	r0, r0, #5
	add	sp, sp, #20
	@ sp needed
	ldr	pc, [sp], #4
.L59:
	.align	2
.L58:
	.word	.LANCHOR0
	.word	.LANCHOR2
	.size	erase_source, .-erase_source
	.section	.text.flash.constprop.0,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	flash.constprop.0, %function
flash.constprop.0:
	@ args = 0, pretend = 0, frame = 16
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, r3, r4, lr}
	movs	r3, #1
	strd	r2, r1, [sp, #8]
	str	r0, [sp, #4]
	ldr	r2, .L61
	strb	r3, [sp]
	mov	r1, sp
	mov	r0, r3
	bl	mesh_flash_op_push
	add	sp, sp, #20
	@ sp needed
	ldr	pc, [sp], #4
.L62:
	.align	2
.L61:
	.word	.LANCHOR2
	.size	flash.constprop.0, .-flash.constprop.0
	.section	.text.invalidate_duplicate_entries,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	invalidate_duplicate_entries, %function
invalidate_duplicate_entries:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, r7, r8, r9, r10, lr}
	ldr	r6, .L74
	ldr	r0, [r6, #12]
	ldrb	r3, [r0, #4]	@ zero_extendqisi2
	ldrb	r2, [r0, #5]	@ zero_extendqisi2
	subs	r3, r3, #1
	cmp	r2, r3
	bne	.L64
	movs	r0, #1
	strb	r0, [r6, #25]
.L65:
	pop	{r4, r5, r6, r7, r8, r9, r10, pc}
.L64:
	add	r3, r0, #4096
	ldr	r8, .L74+4
	ldrb	r4, [r3]	@ zero_extendqisi2
	add	r4, r4, r3
	ldr	r3, [r8]
	ldrb	r5, [r3, #4]!	@ zero_extendqisi2
	add	r5, r5, r3
	bl	get_last_page
	ldrh	r3, [r4, #2]
	subs	r3, r3, #1
	uxth	r3, r3
	movw	r2, #32510
	cmp	r3, r2
	add	r7, r0, #4096
	bls	.L66
	mov	r0, r4
	mov	r1, r7
	bl	get_next_data_entry
	mov	r4, r0
.L66:
	ldr	r10, .L74+8
	mov	r9, #1
.L67:
	cbnz	r4, .L69
.L68:
	clz	r4, r4
	lsrs	r4, r4, #5
	strb	r4, [r6, #25]
	movs	r0, #1
	b	.L65
.L69:
	ldr	r1, [r8]
	ldrh	r2, [r4, #2]
	mov	r0, r5
	add	r1, r1, #4096
	bl	entry_get
	mov	r5, r0
	cmp	r0, #0
	beq	.L68
	movs	r2, #4
	mov	r1, r10
	mov	r0, r4
	strb	r9, [r6, #24]
	bl	flash.constprop.0
	cbnz	r0, .L70
	mov	r0, r4
	mov	r1, r7
	bl	get_next_data_entry
	mov	r4, r0
	b	.L67
.L70:
	movs	r0, #0
	b	.L65
.L75:
	.align	2
.L74:
	.word	.LANCHOR0
	.word	.LANCHOR3
	.word	INVALID_HEADER
	.size	invalidate_duplicate_entries, .-invalidate_duplicate_entries
	.section	.text.seal_storage_page,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	seal_storage_page, %function
seal_storage_page:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, lr}
	ldr	r4, .L83
	ldr	r3, [r4, #12]
	ldrb	r0, [r3]	@ zero_extendqisi2
	movw	r2, #65535
	add	r1, r3, #4096
	add	r0, r0, r3
	bl	entry_get
	cbz	r0, .L80
	ldr	r3, [r4, #12]
	ldrb	r1, [r3]	@ zero_extendqisi2
	add	r3, r3, r1
	cmp	r0, r3
	beq	.L80
	ldrb	r5, [r4, #25]	@ zero_extendqisi2
	ldr	r1, .L83+4
	ldr	r3, .L83+8
	movs	r2, #4
	cmp	r5, #0
	it	eq
	moveq	r1, r3
	bl	flash.constprop.0
	cbnz	r0, .L82
	movs	r0, #1
	strb	r0, [r4, #24]
.L77:
	pop	{r3, r4, r5, pc}
.L80:
	movs	r0, #1
	b	.L77
.L82:
	movs	r0, #0
	b	.L77
.L84:
	.align	2
.L83:
	.word	.LANCHOR0
	.word	SEAL_HEADER
	.word	PADDING_HEADER
	.size	seal_storage_page, .-seal_storage_page
	.section	.text.copy_metadata,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	copy_metadata, %function
copy_metadata:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	ldr	r5, .L88
	ldr	r6, .L88+4
	ldr	r1, [r5, #12]
	ldr	r0, [r6]
	ldrb	r4, [r1]	@ zero_extendqisi2
	adds	r0, r0, #4
	mov	r2, r4
	bl	flash.constprop.0
	cbnz	r0, .L87
	ldr	r2, [r6]
	ldr	r3, [r5, #12]
	and	r4, r4, #252
	adds	r4, r4, #4
	add	r4, r4, r2
	ldrb	r2, [r3]	@ zero_extendqisi2
	str	r4, [r5, #20]
	add	r3, r3, r2
	str	r3, [r5, #16]
	movs	r0, #1
.L86:
	pop	{r4, r5, r6, pc}
.L87:
	movs	r0, #0
	b	.L86
.L89:
	.align	2
.L88:
	.word	.LANCHOR0
	.word	.LANCHOR3
	.size	copy_metadata, .-copy_metadata
	.section	.text.write_defrag_start_pointer,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	write_defrag_start_pointer, %function
write_defrag_start_pointer:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, lr}
	ldr	r3, .L91
	ldr	r1, .L91+4
	ldr	r0, [r3]
	movs	r2, #4
	bl	flash.constprop.0
	clz	r0, r0
	lsrs	r0, r0, #5
	pop	{r3, pc}
.L92:
	.align	2
.L91:
	.word	.LANCHOR3
	.word	.LANCHOR0+12
	.size	write_defrag_start_pointer, .-write_defrag_start_pointer
	.section	.text.write_back,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	write_back, %function
write_back:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	ldr	r3, .L96
	push	{r4, lr}
	ldr	r1, [r3]
	ldr	r4, .L96+4
	movw	r2, #4092
	ldr	r0, [r4, #12]
	adds	r1, r1, #4
	bl	flash.constprop.0
	cbnz	r0, .L95
	movs	r0, #1
	strb	r0, [r4, #24]
.L94:
	pop	{r4, pc}
.L95:
	movs	r0, #0
	b	.L94
.L97:
	.align	2
.L96:
	.word	.LANCHOR3
	.word	.LANCHOR0
	.size	write_back, .-write_back
	.section	.text.post_process,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	post_process, %function
post_process:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	ldr	r4, .L102
	ldr	r1, [r4, #12]
	mov	r0, r1
	bl	get_last_page
	cmp	r1, r0
	bne	.L99
	ldr	r3, .L102+4
	ldr	r1, .L102+8
	ldr	r0, [r3]
	movs	r2, #4
	bl	flash.constprop.0
	cbnz	r0, .L101
	movs	r3, #1
	strb	r3, [r4, #24]
	movs	r0, #2
.L100:
	pop	{r4, pc}
.L99:
	add	r1, r1, #4096
	str	r1, [r4, #12]
	movs	r0, #3
	b	.L100
.L101:
	movs	r0, #0
	b	.L100
.L103:
	.align	2
.L102:
	.word	.LANCHOR0
	.word	.LANCHOR3
	.word	.LANCHOR4
	.size	post_process, .-post_process
	.section	.text.backup_entries,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	backup_entries, %function
backup_entries:
	@ args = 0, pretend = 0, frame = 8
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, r4, r5, r6, r7, r8, r9, r10, fp, lr}
	ldr	r5, .L129
	ldr	r3, [r5, #16]
	cbnz	r3, .L105
	.syntax unified
@ 263 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L105:
	ldr	r3, [r5, #20]
	cbnz	r3, .L106
	.syntax unified
@ 264 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L106:
	ldr	r9, .L129+4
	movw	r10, #32510
.L117:
	ldr	r3, [r5, #20]
	ldrd	r0, r6, [r5, #12]
	and	r8, r3, r9
	sub	r8, r8, r3
	bl	get_last_page
	ldrh	r3, [r6, #2]
	subs	r3, r3, #1
	uxth	r3, r3
	cmp	r3, r10
	add	r8, r8, #4096
	add	fp, r0, #4096
	bls	.L107
	mov	r0, r6
	mov	r1, fp
	bl	get_next_data_entry
	mov	r6, r0
	cmp	r0, #0
	beq	.L121
.L107:
	mov	r4, r6
	movs	r7, #0
.L109:
	cmp	r4, fp
	bcs	.L110
	ldrh	r2, [r4]
	add	r2, r7, r2, lsl #2
	cmp	r8, r2
	bls	.L111
	eor	r3, r6, r4
	tst	r3, r9
	bne	.L111
	ldrh	r3, [r4, #2]
	subs	r3, r3, #1
	uxth	r3, r3
	cmp	r3, r10
	bls	.L112
.L111:
	cbnz	r7, .L118
	movs	r3, #1
	b	.L119
.L112:
	mov	r0, r4
	str	r2, [sp, #4]
	bl	get_next_entry
	ldr	r2, [sp, #4]
	mov	r4, r0
	mov	r7, r2
	b	.L109
.L110:
	cbz	r7, .L120
.L118:
	ldr	r0, [r5, #20]
	mov	r2, r7
	mov	r1, r6
	bl	flash.constprop.0
	cbnz	r0, .L114
	ldr	r3, [r5, #20]
	add	r3, r3, r7
	str	r3, [r5, #20]
	cbnz	r4, .L115
	.syntax unified
@ 284 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L115:
	str	r4, [r5, #16]
	movs	r3, #0
.L113:
	cbz	r4, .L121
.L119:
	ldrh	r1, [r4, #2]
	movw	r2, #32767
	cmp	r1, r2
	beq	.L121
	cmp	r3, #0
	beq	.L117
.L121:
	movs	r0, #1
	b	.L128
.L114:
	movs	r0, #0
.L128:
	add	sp, sp, #12
	@ sp needed
	pop	{r4, r5, r6, r7, r8, r9, r10, fp, pc}
.L120:
	movs	r3, #1
	b	.L113
.L130:
	.align	2
.L129:
	.word	.LANCHOR0
	.word	-4096
	.size	backup_entries, .-backup_entries
	.section	.text.erase_recovery_area,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	erase_recovery_area, %function
erase_recovery_area:
	@ args = 0, pretend = 0, frame = 16
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, r3, r4, lr}
	ldr	r3, .L132
	movs	r2, #2
	ldr	r3, [r3]
	strb	r2, [sp]
	str	r3, [sp, #4]
	ldr	r2, .L132+4
	mov	r3, #4096
	mov	r1, sp
	movs	r0, #1
	str	r3, [sp, #8]
	bl	mesh_flash_op_push
	clz	r0, r0
	lsrs	r0, r0, #5
	add	sp, sp, #20
	@ sp needed
	ldr	pc, [sp], #4
.L133:
	.align	2
.L132:
	.word	.LANCHOR3
	.word	.LANCHOR2
	.size	erase_recovery_area, .-erase_recovery_area
	.section	.rodata.flash_manager_defrag_init.str1.1,"aMS",%progbits,1
.LC0:
	.ascii	"C:\\Users\\glu250\\Downloads\\myic\\nrf5_SDK_for_Me"
	.ascii	"sh_v5.0.0_src\\mesh\\core\\src\\flash_manager_defra"
	.ascii	"g.c\000"
.LC1:
	.ascii	"BOOTLOADERADDR(): 0x%08x fm_recovery_area: 0x%08x\012"
	.ascii	"\000"
	.section	.text.flash_manager_defrag_init,"ax",%progbits
	.align	1
	.global	flash_manager_defrag_init
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	flash_manager_defrag_init, %function
flash_manager_defrag_init:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, r3, r4, lr}
	movs	r3, #0
	ldr	r2, .L152
	ldr	r1, [r3, #4088]
	strb	r3, [r2]
	adds	r2, r1, #1
	bne	.L135
	mov	r3, #268439552
	ldr	r2, [r3, #20]
	adds	r2, r2, #1
	beq	.L136
	ldr	r2, [r3, #20]
	cbnz	r2, .L137
.L136:
	mov	r3, #268435456
	ldr	r2, [r3, #20]
	ldr	r3, [r3, #16]
	muls	r2, r3, r2
	b	.L140
.L135:
	cmp	r1, #0
	beq	.L136
	sub	r2, r1, #4096
	b	.L140
.L137:
	ldr	r2, [r3, #20]
	sub	r2, r2, #4096
.L140:
	ldr	r3, .L152+4
	ldr	r4, .L152+8
	ldr	r3, [r3]
	sub	r2, r2, #4096
	lsls	r3, r3, #11
	str	r2, [r4]
	bpl	.L141
	ldr	r3, .L152+12
	ldr	r3, [r3]
	cmp	r3, #6
	ble	.L141
	adds	r0, r1, #1
	it	eq
	moveq	r1, #268439552
	ldr	r3, .L152+16
	ldr	r3, [r3, #1284]
	it	eq
	ldreq	r1, [r1, #20]
	strd	r1, r2, [sp, #4]
	ldr	r2, .L152+20
	str	r2, [sp]
	ldr	r1, .L152+24
	movw	r2, #630
	movs	r0, #7
	bl	log_printf
.L141:
	ldr	r3, [r4]
	ldr	r1, [r3]
	subs	r3, r1, #1
	adds	r3, r3, #3
	bhi	.L145
	ubfx	r2, r1, #0, #12
	cbnz	r2, .L145
	ldr	r3, .L152+28
	ldr	r0, .L152+32
	strh	r2, [r3, #24]	@ movhi
	movs	r4, #1
	str	r1, [r3, #12]
	strb	r4, [r3]
	str	r2, [r3, #8]
	bl	jump_to_step
	mov	r0, r4
	ldr	r1, .L152+36
	bl	mesh_flash_user_callback_set
	bl	execute_procedure_step
	mov	r0, r4
.L143:
	add	sp, sp, #16
	@ sp needed
	pop	{r4, pc}
.L145:
	movs	r0, #0
	b	.L143
.L153:
	.align	2
.L152:
	.word	.LANCHOR5
	.word	g_log_dbg_msk
	.word	.LANCHOR3
	.word	g_log_dbg_lvl
	.word	1073811456
	.word	.LC1
	.word	.LC0+74
	.word	.LANCHOR0
	.word	erase_source
	.word	on_flash_op_end
	.size	flash_manager_defrag_init, .-flash_manager_defrag_init
	.section	.text.flash_manager_defragging,"ax",%progbits
	.align	1
	.global	flash_manager_defragging
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	flash_manager_defragging, %function
flash_manager_defragging:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	mov	r4, r0
	cbnz	r0, .L155
	.syntax unified
@ 637 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L155:
	ldr	r2, .L159
	ldrb	r0, [r2]	@ zero_extendqisi2
	cbz	r0, .L156
	ldr	r0, [r4, #12]
	ldr	r1, [r2, #12]
	ldrb	r3, [r0, #5]	@ zero_extendqisi2
	sub	r3, r0, r3, lsl #12
	cmp	r1, r3
	bcc	.L158
	bl	get_last_page
	cmp	r1, r0
	ite	hi
	movhi	r0, #0
	movls	r0, #1
.L156:
	pop	{r4, pc}
.L158:
	movs	r0, #0
	b	.L156
.L160:
	.align	2
.L159:
	.word	.LANCHOR0
	.size	flash_manager_defragging, .-flash_manager_defragging
	.section	.text.flash_manager_defrag_is_running,"ax",%progbits
	.align	1
	.global	flash_manager_defrag_is_running
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	flash_manager_defrag_is_running, %function
flash_manager_defrag_is_running:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r3, .L162
	ldrb	r0, [r3]	@ zero_extendqisi2
	subs	r0, r0, #0
	it	ne
	movne	r0, #1
	bx	lr
.L163:
	.align	2
.L162:
	.word	.LANCHOR0
	.size	flash_manager_defrag_is_running, .-flash_manager_defrag_is_running
	.section	.text.flash_manager_defrag,"ax",%progbits
	.align	1
	.global	flash_manager_defrag
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	flash_manager_defrag, %function
flash_manager_defrag:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r3, r4, r5, lr}
	ldr	r4, .L175
	ldrb	r3, [r4]	@ zero_extendqisi2
	mov	r5, r0
	cbz	r3, .L165
	.syntax unified
@ 650 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L165:
	ldrb	r3, [r5]	@ zero_extendqisi2
	cmp	r3, #3
	beq	.L166
	.syntax unified
@ 651 "C:\Users\glu250\Downloads\myic\nrf5_SDK_for_Mesh_v5.0.0_src\mesh\core\src\flash_manager_defrag.c" 1
	mov r0, pc
	
@ 0 "" 2
	.thumb
	.syntax unified
	bl	mesh_assertion_handler
.L166:
	ldr	r3, [r5, #12]
	str	r3, [r4, #12]
	ldr	r3, .L175+4
	ldr	r1, .L175+8
	ldrb	r3, [r3]	@ zero_extendqisi2
	str	r5, [r4, #8]
	cmp	r3, #0
	ite	ne
	movne	r3, #10
	moveq	r3, #0
	str	r3, [r4, #4]
	movs	r0, #1
	movs	r3, #0
	strb	r0, [r4]
	strh	r3, [r4, #24]	@ movhi
	bl	mesh_flash_user_callback_set
	pop	{r3, r4, r5, lr}
	b	execute_procedure_step
.L176:
	.align	2
.L175:
	.word	.LANCHOR0
	.word	.LANCHOR5
	.word	on_flash_op_end
	.size	flash_manager_defrag, .-flash_manager_defrag
	.section	.text.flash_manager_defrag_recovery_page_get,"ax",%progbits
	.align	1
	.global	flash_manager_defrag_recovery_page_get
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	flash_manager_defrag_recovery_page_get, %function
flash_manager_defrag_recovery_page_get:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r3, .L178
	ldr	r0, [r3]
	bx	lr
.L179:
	.align	2
.L178:
	.word	.LANCHOR3
	.size	flash_manager_defrag_recovery_page_get, .-flash_manager_defrag_recovery_page_get
	.section	.text.flash_manager_defrag_freeze,"ax",%progbits
	.align	1
	.global	flash_manager_defrag_freeze
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	flash_manager_defrag_freeze, %function
flash_manager_defrag_freeze:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r3, .L181
	ldr	r0, .L181+4
	movs	r2, #1
	strb	r2, [r3]
	b	jump_to_step
.L182:
	.align	2
.L181:
	.word	.LANCHOR5
	.word	freezing
	.size	flash_manager_defrag_freeze, .-flash_manager_defrag_freeze
	.section	.bss.m_defrag,"aw",%nobits
	.align	2
	.set	.LANCHOR0,. + 0
	.type	m_defrag, %object
	.size	m_defrag, 28
m_defrag:
	.space	28
	.section	.bss.m_is_frozen,"aw",%nobits
	.set	.LANCHOR5,. + 0
	.type	m_is_frozen, %object
	.size	m_is_frozen, 1
m_is_frozen:
	.space	1
	.section	.bss.m_token,"aw",%nobits
	.align	1
	.set	.LANCHOR2,. + 0
	.type	m_token, %object
	.size	m_token, 2
m_token:
	.space	2
	.section	.bss.mp_recovery_area,"aw",%nobits
	.align	2
	.set	.LANCHOR3,. + 0
	.type	mp_recovery_area, %object
	.size	mp_recovery_area, 4
mp_recovery_area:
	.space	4
	.section	.bss.p_null_ptr.0,"aw",%nobits
	.align	2
	.set	.LANCHOR4,. + 0
	.type	p_null_ptr.0, %object
	.size	p_null_ptr.0, 4
p_null_ptr.0:
	.space	4
	.section	.rodata.m_procedure_steps,"a"
	.align	2
	.set	.LANCHOR1,. + 0
	.type	m_procedure_steps, %object
	.size	m_procedure_steps, 44
m_procedure_steps:
	.word	check_for_invalid_entries
	.word	erase_recovery_area
	.word	copy_metadata
	.word	backup_entries
	.word	write_defrag_start_pointer
	.word	erase_source
	.word	write_back
	.word	invalidate_duplicate_entries
	.word	seal_storage_page
	.word	post_process
	.word	freezing
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
