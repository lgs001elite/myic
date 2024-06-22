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
	.file	"mesh_app_utils.c"
	.text
	.section	.rodata.mesh_app_uuid_print.str1.1,"aMS",%progbits,1
.LC0:
	.ascii	"C:\\Users\\glu250\\Downloads\\myic\\nrf5_SDK_for_Me"
	.ascii	"sh_v5.0.0_src\\examples\\common\\src\\mesh_app_util"
	.ascii	"s.c\000"
.LC1:
	.ascii	"Device UUID (raw)\000"
.LC2:
	.ascii	"%s: %s\012\000"
.LC3:
	.ascii	"Device UUID : %08X-%04X-%04X-%02X%02X-%02X%02X%02X%"
	.ascii	"02X%02X%02X\012\000"
	.section	.text.mesh_app_uuid_print,"ax",%progbits
	.align	1
	.global	mesh_app_uuid_print
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	mesh_app_uuid_print, %function
mesh_app_uuid_print:
	@ args = 0, pretend = 0, frame = 264
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, r7, lr}
	mov	r4, r0
	sub	sp, sp, #316
	cbz	r0, .L1
	ldr	r6, .L13
	ldr	r3, [r6]
	lsls	r2, r3, #17
	bpl	.L1
	ldr	r7, .L13+4
	ldr	r3, [r7]
	cmp	r3, #3
	bgt	.L5
.L1:
	add	sp, sp, #316
	@ sp needed
	pop	{r4, r5, r6, r7, pc}
.L5:
	ldr	r3, .L13+8
	ldr	r5, [r3]
	add	r3, sp, #52
	subs	r1, r0, #1
	add	ip, r0, #15
	mov	r0, r3
.L7:
	ldrb	r2, [r1, #1]!	@ zero_extendqisi2
	lsr	lr, r2, #4
	and	r2, r2, #15
	ldrb	lr, [r5, lr]	@ zero_extendqisi2
	strb	lr, [r3]
	ldrb	r2, [r5, r2]	@ zero_extendqisi2
	strb	r2, [r3, #1]
	cmp	r1, ip
	add	r3, r3, #2
	bne	.L7
	movs	r3, #0
	ldr	r5, .L13+12
	strb	r3, [r0, #32]
	ldr	r2, .L13+16
	ldr	r3, [r5, #1284]
	str	r2, [sp, #4]
	ldr	r2, .L13+20
	str	r0, [sp, #8]
	str	r2, [sp]
	ldr	r1, .L13+24
	movs	r2, #66
	movs	r0, #4
	bl	log_printf
	ldr	r3, [r6]
	lsls	r3, r3, #17
	bpl	.L1
	ldr	r3, [r7]
	cmp	r3, #3
	ble	.L1
	ldrb	r2, [r4, #15]	@ zero_extendqisi2
	ldr	r1, [r4]	@ unaligned
	ldr	r3, [r5, #1284]
	str	r2, [sp, #44]
	ldrb	r2, [r4, #14]	@ zero_extendqisi2
	str	r2, [sp, #40]
	ldrb	r2, [r4, #13]	@ zero_extendqisi2
	str	r2, [sp, #36]
	ldrb	r2, [r4, #12]	@ zero_extendqisi2
	str	r2, [sp, #32]
	ldrb	r2, [r4, #11]	@ zero_extendqisi2
	str	r2, [sp, #28]
	ldrb	r2, [r4, #10]	@ zero_extendqisi2
	str	r2, [sp, #24]
	ldrb	r2, [r4, #9]	@ zero_extendqisi2
	str	r2, [sp, #20]
	ldrb	r2, [r4, #8]	@ zero_extendqisi2
	str	r2, [sp, #16]
	ldrh	r2, [r4, #6]	@ unaligned
	rev16	r2, r2
	uxth	r2, r2
	str	r2, [sp, #12]
	ldrh	r2, [r4, #4]	@ unaligned
	rev16	r2, r2
	rev	r1, r1
	uxth	r2, r2
	strd	r1, r2, [sp, #4]
	ldr	r2, .L13+28
	str	r2, [sp]
	ldr	r1, .L13+24
	movs	r2, #67
	movs	r0, #4
	bl	log_printf
	b	.L1
.L14:
	.align	2
.L13:
	.word	g_log_dbg_msk
	.word	g_log_dbg_lvl
	.word	g_log_hex_digits
	.word	1073811456
	.word	.LC1
	.word	.LC2
	.word	.LC0+80
	.word	.LC3
	.size	mesh_app_uuid_print, .-mesh_app_uuid_print
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
