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
	.file	"nrf_mesh_configure.c"
	.text
	.section	.text.nrf_mesh_configure_device_uuid_set,"ax",%progbits
	.align	1
	.global	nrf_mesh_configure_device_uuid_set
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	nrf_mesh_configure_device_uuid_set, %function
nrf_mesh_configure_device_uuid_set:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r3, .L4
	add	r2, r0, #16
.L2:
	ldr	r1, [r0], #4	@ unaligned
	str	r1, [r3], #4	@ unaligned
	cmp	r0, r2
	bne	.L2
	bx	lr
.L5:
	.align	2
.L4:
	.word	.LANCHOR0
	.size	nrf_mesh_configure_device_uuid_set, .-nrf_mesh_configure_device_uuid_set
	.section	.text.nrf_mesh_configure_device_uuid_reset,"ax",%progbits
	.align	1
	.global	nrf_mesh_configure_device_uuid_reset
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	nrf_mesh_configure_device_uuid_reset, %function
nrf_mesh_configure_device_uuid_reset:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	mov	r2, #268435456
	add	r4, r2, #96
	ldmia	r4!, {r0, r1}
	ldr	r3, .L7
	adds	r2, r2, #164
	str	r1, [r3, #4]	@ unaligned
	str	r0, [r3]	@ unaligned
	ldmia	r2!, {r0, r1}
	ldrb	r2, [r3, #6]	@ zero_extendqisi2
	str	r0, [r3, #8]	@ unaligned
	and	r2, r2, #15
	orr	r2, r2, #64
	strb	r2, [r3, #6]
	ldrb	r2, [r3, #8]	@ zero_extendqisi2
	str	r1, [r3, #12]	@ unaligned
	and	r2, r2, #63
	orn	r2, r2, #127
	strb	r2, [r3, #8]
	pop	{r4, pc}
.L8:
	.align	2
.L7:
	.word	.LANCHOR0
	.size	nrf_mesh_configure_device_uuid_reset, .-nrf_mesh_configure_device_uuid_reset
	.section	.text.nrf_mesh_configure_device_uuid_get,"ax",%progbits
	.align	1
	.global	nrf_mesh_configure_device_uuid_get
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	nrf_mesh_configure_device_uuid_get, %function
nrf_mesh_configure_device_uuid_get:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	ldr	r0, .L10
	bx	lr
.L11:
	.align	2
.L10:
	.word	.LANCHOR0
	.size	nrf_mesh_configure_device_uuid_get, .-nrf_mesh_configure_device_uuid_get
	.section	.bss.m_uuid,"aw",%nobits
	.set	.LANCHOR0,. + 0
	.type	m_uuid, %object
	.size	m_uuid, 16
m_uuid:
	.space	16
	.ident	"GCC: (GNU) 10.2.1 20201103 (release)"
