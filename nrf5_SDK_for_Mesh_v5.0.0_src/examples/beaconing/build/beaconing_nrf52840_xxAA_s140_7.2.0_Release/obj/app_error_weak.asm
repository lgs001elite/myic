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
	.file	"app_error_weak.c"
	.text
	.section	.rodata.app_error_fault_handler.str1.1,"aMS",%progbits,1
.LC0:
	.ascii	"/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0."
	.ascii	"0_src/examples/common/src/app_error_weak.c\000"
.LC1:
	.ascii	"Softdevice assert: %u:%u\012\000"
.LC2:
	.ascii	"Application memory access: %u:%u\012\000"
.LC3:
	.ascii	"Mesh assert at 0x%08x (%s:%u)\012\000"
.LC4:
	.ascii	"Mesh error %u at 0x%08x (%s:%u)\012\000"
.LC5:
	.ascii	"UNKNOWN FAULT at 0x%08X\012\000"
	.section	.text.app_error_fault_handler,"ax",%progbits
	.align	1
	.weak	app_error_fault_handler
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	app_error_fault_handler, %function
app_error_fault_handler:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, lr}
	ldr	r3, .L27
	movw	r5, #16385
	ldr	r3, [r3]
	cmp	r0, r5
	sub	sp, sp, #28
	mov	r4, r0
	and	r3, r3, #16384
	beq	.L2
	bhi	.L3
	cmp	r0, #1
	beq	.L4
	movw	r0, #4097
	cmp	r4, r0
	beq	.L5
.L6:
	cmp	r3, #0
	beq	.L8
	ldr	r3, .L27+4
	ldr	r3, [r3]
	cmp	r3, #0
	ble	.L8
	ldr	r3, .L27+8
	ldr	r2, .L27+12
	ldr	r3, [r3, #1284]
	str	r1, [sp, #4]
	str	r2, [sp]
	ldr	r1, .L27+16
	movs	r2, #123
	movs	r0, #1
	bl	log_printf
	b	.L8
.L3:
	movw	r0, #16386
	cmp	r4, r0
	bne	.L6
	cbz	r3, .L8
	ldr	r3, .L27+4
	ldr	r3, [r3]
	cmp	r3, #0
	ble	.L8
	ldr	r3, .L27+8
	ldr	r0, [r2]
	ldr	r3, [r3, #1284]
	str	r0, [sp, #12]
	ldr	r2, [r2, #4]
	strd	r1, r2, [sp, #4]
	ldr	r2, .L27+20
	str	r2, [sp]
	ldr	r1, .L27+16
	movs	r2, #105
	movs	r0, #1
	bl	log_printf
	b	.L8
.L4:
	cbz	r3, .L8
	ldr	r3, .L27+4
	ldr	r3, [r3]
	cmp	r3, #0
	ble	.L8
	ldr	r3, .L27+8
	ldr	r3, [r3, #1284]
	strd	r1, r2, [sp, #4]
	ldr	r2, .L27+24
	ldr	r1, .L27+16
	str	r2, [sp]
	movs	r2, #96
.L26:
	bl	log_printf
.L8:
	mov	r3, #1342177280
	mov	r2, #122880
	str	r2, [r3, #1304]
	str	r2, [r3, #1292]
	.syntax unified
@ 72 "/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0.0_src/examples/common/src/app_error_weak.c" 1
	MRS r3, primask
@ 0 "" 2
@ 72 "/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0.0_src/examples/common/src/app_error_weak.c" 1
	cpsid i
@ 0 "" 2
@ 74 "/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0.0_src/examples/common/src/app_error_weak.c" 1
	MOV R12, #0xDEAD

@ 0 "" 2
	.thumb
	.syntax unified
	ldr	r2, .L27+28
.L9:
	ldrb	r3, [r2]	@ zero_extendqisi2
	cmp	r3, #0
	bne	.L10
	add	sp, sp, #28
	@ sp needed
	pop	{r4, r5, pc}
.L5:
	cmp	r3, #0
	beq	.L8
	ldr	r3, .L27+4
	ldr	r3, [r3]
	cmp	r3, #0
	ble	.L8
	ldr	r3, .L27+8
	ldr	r3, [r3, #1284]
	strd	r1, r2, [sp, #4]
	ldr	r2, .L27+32
	str	r2, [sp]
	ldr	r1, .L27+16
	movs	r2, #99
	movs	r0, #1
	b	.L26
.L2:
	cmp	r3, #0
	beq	.L8
	ldr	r3, .L27+4
	ldr	r3, [r3]
	cmp	r3, #0
	ble	.L8
	ldr	r3, .L27+8
	ldr	r0, [r2]
	ldr	r3, [r3, #1284]
	str	r0, [sp, #16]
	ldr	r0, [r2, #4]
	strd	r1, r0, [sp, #8]
	ldr	r2, [r2, #8]
	str	r2, [sp, #4]
	ldr	r2, .L27+36
	str	r2, [sp]
	ldr	r1, .L27+16
	movs	r2, #115
	movs	r0, #1
	bl	log_printf
	b	.L8
.L10:
	.syntax unified
@ 81 "/home/gaosheng/mesh/my_mesh/nrf5_SDK_for_Mesh_v5.0.0_src/examples/common/src/app_error_weak.c" 1
	wfi
@ 0 "" 2
	.thumb
	.syntax unified
	b	.L9
.L28:
	.align	2
.L27:
	.word	g_log_dbg_msk
	.word	g_log_dbg_lvl
	.word	1073811456
	.word	.LC5
	.word	.LC0+77
	.word	.LC3
	.word	.LC1
	.word	.LANCHOR0
	.word	.LC2
	.word	.LC4
	.size	app_error_fault_handler, .-app_error_fault_handler
	.section	.data.wait.0,"aw"
	.set	.LANCHOR0,. + 0
	.type	wait.0, %object
	.size	wait.0, 1
wait.0:
	.byte	1
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
