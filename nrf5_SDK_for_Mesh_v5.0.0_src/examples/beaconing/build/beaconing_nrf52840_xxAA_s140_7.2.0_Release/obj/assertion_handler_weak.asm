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
	.file	"assertion_handler_weak.c"
	.text
	.section	.rodata.mesh_assertion_handler.str1.1,"aMS",%progbits,1
.LC0:
	.ascii	"\000"
	.section	.text.mesh_assertion_handler,"ax",%progbits
	.align	1
	.weak	mesh_assertion_handler
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_assertion_handler, %function
mesh_assertion_handler:
	@ args = 0, pretend = 0, frame = 8
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r0, r1, r2, lr}
	movs	r3, #0
	mov	r1, r0
	str	r3, [sp]
	mov	r2, sp
	ldr	r3, .L2
	str	r3, [sp, #4]
	movw	r0, #16386
	bl	app_error_fault_handler
	add	sp, sp, #12
	@ sp needed
	ldr	pc, [sp], #4
.L3:
	.align	2
.L2:
	.word	.LC0
	.size	mesh_assertion_handler, .-mesh_assertion_handler
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
