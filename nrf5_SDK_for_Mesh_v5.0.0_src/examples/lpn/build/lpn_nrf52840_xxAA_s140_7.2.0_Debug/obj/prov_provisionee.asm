	.cpu cortex-m4
	.arch armv7e-m
	.fpu fpv4-sp-d16
	.eabi_attribute 27, 1
	.eabi_attribute 28, 1
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 1
	.eabi_attribute 30, 1
	.eabi_attribute 34, 1
	.eabi_attribute 38, 1
	.eabi_attribute 18, 4
	.file	"prov_provisionee.c"
	.text
.Ltext0:
	.file 1 "C:\\Users\\glu250\\Downloads\\Next\\myic\\nrf5_SDK_for_Mesh_v5.0.0_src\\mesh\\prov\\src\\prov_provisionee.c"
	.section	.text.complete_provisioning,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.type	complete_provisioning, %function
complete_provisioning:
.LVL0:
.LFB432:
	.loc 1 570 1 view -0
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 1 570 1 is_stmt 0 view .LVU1
	push	{lr}
.LCFI0:
	sub	sp, sp, #36
.LCFI1:
	.loc 1 571 5 is_stmt 1 view .LVU2
	.loc 1 572 5 view .LVU3
	.loc 1 572 20 is_stmt 0 view .LVU4
	movs	r3, #10
	strb	r3, [sp]
	.loc 1 573 5 is_stmt 1 view .LVU5
	.loc 1 573 41 is_stmt 0 view .LVU6
	str	r0, [sp, #4]
	.loc 1 574 5 is_stmt 1 view .LVU7
	.loc 1 574 42 is_stmt 0 view .LVU8
	add	r3, r0, #120
	.loc 1 574 40 view .LVU9
	str	r3, [sp, #8]
	.loc 1 575 5 is_stmt 1 view .LVU10
	.loc 1 575 45 is_stmt 0 view .LVU11
	add	r3, r0, #280
	.loc 1 575 43 view .LVU12
	str	r3, [sp, #12]
	.loc 1 576 5 is_stmt 1 view .LVU13
	.loc 1 576 10 is_stmt 0 view .LVU14
	ldr	r3, [r0, #12]
	.loc 1 576 5 view .LVU15
	mov	r0, sp
.LVL1:
	.loc 1 576 5 view .LVU16
	blx	r3
.LVL2:
	.loc 1 577 1 view .LVU17
	add	sp, sp, #36
.LCFI2:
	@ sp needed
	ldr	pc, [sp], #4
.LFE432:
	.size	complete_provisioning, .-complete_provisioning
	.section	.text.prov_provisionee_cb_link_established,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.type	prov_provisionee_cb_link_established, %function
prov_provisionee_cb_link_established:
.LVL3:
.LFB434:
	.loc 1 616 1 is_stmt 1 view -0
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 1 616 1 is_stmt 0 view .LVU19
	push	{r4, r5, r6, lr}
.LCFI3:
	sub	sp, sp, #32
.LCFI4:
	mov	r5, r0
	.loc 1 617 5 is_stmt 1 view .LVU20
.LVL4:
.LBB25:
.LBI25:
	.file 2 "../../mesh/prov/include/provisioning.h"
	.loc 2 69 37 view .LVU21
.LBB26:
	.loc 2 71 5 view .LVU22
	.loc 2 71 12 is_stmt 0 view .LVU23
	ldr	r6, [r0, #16]
.LVL5:
	.loc 2 71 12 view .LVU24
.LBE26:
.LBE25:
	.loc 1 618 5 is_stmt 1 view .LVU25
	.loc 1 618 28 is_stmt 0 view .LVU26
	str	r0, [r6, #8]
	.loc 1 620 5 is_stmt 1 view .LVU27
	.loc 1 621 5 view .LVU28
.LBB27:
	.loc 1 621 5 view .LVU29
	ldr	r4, [r6]
.LVL6:
	.loc 1 621 5 is_stmt 0 view .LVU30
	b	.L4
.LVL7:
.L9:
	.loc 1 626 13 is_stmt 1 view .LVU31
	.loc 1 626 32 is_stmt 0 view .LVU32
	ldr	r3, [r4, #8]
	.loc 1 626 45 view .LVU33
	ldr	r3, [r3, #8]
	.loc 1 626 20 view .LVU34
	mov	r0, r4
	blx	r3
.LVL8:
.L5:
	.loc 1 621 5 is_stmt 1 discriminator 2 view .LVU35
	ldr	r4, [r4]
.LVL9:
.L4:
	.loc 1 621 5 discriminator 1 view .LVU36
	cbz	r4, .L8
	.loc 1 623 9 view .LVU37
.LVL10:
	.loc 1 624 9 view .LVU38
	.loc 1 624 12 is_stmt 0 view .LVU39
	cmp	r4, r5
	bne	.L9
	b	.L5
.LVL11:
.L8:
	.loc 1 624 12 view .LVU40
.LBE27:
	.loc 1 630 5 is_stmt 1 view .LVU41
	.loc 1 630 18 is_stmt 0 view .LVU42
	movs	r3, #2
	strb	r3, [r6, #267]
	.loc 1 631 5 is_stmt 1 view .LVU43
	.loc 1 632 5 view .LVU44
	.loc 1 632 20 is_stmt 0 view .LVU45
	movs	r3, #1
	strb	r3, [sp]
	.loc 1 633 5 is_stmt 1 view .LVU46
	.loc 1 633 49 is_stmt 0 view .LVU47
	str	r6, [sp, #4]
	.loc 1 634 5 is_stmt 1 view .LVU48
	.loc 1 634 10 is_stmt 0 view .LVU49
	ldr	r3, [r6, #12]
	.loc 1 634 5 view .LVU50
	mov	r0, sp
	blx	r3
.LVL12:
	.loc 1 635 1 view .LVU51
	add	sp, sp, #32
.LCFI5:
	@ sp needed
	pop	{r4, r5, r6, pc}
	.loc 1 635 1 view .LVU52
.LFE434:
	.size	prov_provisionee_cb_link_established, .-prov_provisionee_cb_link_established
	.section	.text.prov_provisionee_cb_link_closed,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.type	prov_provisionee_cb_link_closed, %function
prov_provisionee_cb_link_closed:
.LVL13:
.LFB435:
	.loc 1 637 1 is_stmt 1 view -0
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 1 637 1 is_stmt 0 view .LVU54
	push	{r4, r5, lr}
.LCFI6:
	sub	sp, sp, #36
.LCFI7:
	mov	r5, r1
	.loc 1 638 5 is_stmt 1 view .LVU55
.LVL14:
.LBB28:
.LBI28:
	.loc 2 69 37 view .LVU56
.LBB29:
	.loc 2 71 5 view .LVU57
	.loc 2 71 12 is_stmt 0 view .LVU58
	ldr	r4, [r0, #16]
.LVL15:
	.loc 2 71 12 view .LVU59
.LBE29:
.LBE28:
	.loc 1 639 5 is_stmt 1 view .LVU60
	.loc 1 639 14 is_stmt 0 view .LVU61
	ldrb	r3, [r4, #267]	@ zero_extendqisi2
	.loc 1 639 8 view .LVU62
	cmp	r3, #18
	beq	.L13
.LVL16:
.L11:
	.loc 1 643 5 is_stmt 1 view .LVU63
	.loc 1 643 18 is_stmt 0 view .LVU64
	movs	r3, #0
	strb	r3, [r4, #267]
	.loc 1 644 5 is_stmt 1 view .LVU65
	.loc 1 645 5 view .LVU66
	.loc 1 645 20 is_stmt 0 view .LVU67
	movs	r3, #2
	strb	r3, [sp]
	.loc 1 646 5 is_stmt 1 view .LVU68
	.loc 1 646 44 is_stmt 0 view .LVU69
	str	r4, [sp, #4]
	.loc 1 647 5 is_stmt 1 view .LVU70
	.loc 1 647 47 is_stmt 0 view .LVU71
	strb	r5, [sp, #8]
	.loc 1 648 5 is_stmt 1 view .LVU72
	.loc 1 648 10 is_stmt 0 view .LVU73
	ldr	r3, [r4, #12]
	.loc 1 648 5 view .LVU74
	mov	r0, sp
	blx	r3
.LVL17:
	.loc 1 649 1 view .LVU75
	add	sp, sp, #36
.LCFI8:
	@ sp needed
	pop	{r4, r5, pc}
.LVL18:
.L13:
.LCFI9:
	.loc 1 639 55 discriminator 1 view .LVU76
	cmp	r1, #0
	bne	.L11
	.loc 1 641 9 is_stmt 1 view .LVU77
	mov	r0, r4
.LVL19:
	.loc 1 641 9 is_stmt 0 view .LVU78
	bl	complete_provisioning
.LVL20:
	.loc 1 641 9 view .LVU79
	b	.L11
.LFE435:
	.size	prov_provisionee_cb_link_closed, .-prov_provisionee_cb_link_closed
	.section	.text.request_authentication,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.type	request_authentication, %function
request_authentication:
.LVL21:
.LFB429:
	.loc 1 294 1 is_stmt 1 view -0
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 1 294 1 is_stmt 0 view .LVU81
	push	{r4, r5, lr}
.LCFI10:
	sub	sp, sp, #36
.LCFI11:
	mov	r4, r0
	.loc 1 295 5 is_stmt 1 view .LVU82
.LVL22:
	.loc 1 298 5 view .LVU83
	.loc 1 298 18 is_stmt 0 view .LVU84
	ldrb	r3, [r0, #268]	@ zero_extendqisi2
	.loc 1 298 5 view .LVU85
	cmp	r3, #3
	bhi	.L21
	tbb	[pc, r3]
.L17:
	.byte	(.L20-.L17)/2
	.byte	(.L19-.L17)/2
	.byte	(.L18-.L17)/2
	.byte	(.L16-.L17)/2
	.p2align 1
.L16:
.LBB30:
	.loc 1 302 13 is_stmt 1 view .LVU86
	.loc 1 303 13 view .LVU87
	.loc 1 303 24 is_stmt 0 view .LVU88
	movs	r3, #6
	strb	r3, [sp]
	.loc 1 304 13 is_stmt 1 view .LVU89
	.loc 1 304 50 is_stmt 0 view .LVU90
	str	r0, [sp, #4]
	.loc 1 305 13 is_stmt 1 view .LVU91
	.loc 1 305 52 is_stmt 0 view .LVU92
	ldrb	r3, [r0, #262]	@ zero_extendqisi2
	.loc 1 305 45 view .LVU93
	strb	r3, [sp, #9]
	.loc 1 306 13 is_stmt 1 view .LVU94
	.loc 1 306 54 is_stmt 0 view .LVU95
	ldrb	r3, [r0, #263]	@ zero_extendqisi2
	.loc 1 306 47 view .LVU96
	strb	r3, [sp, #8]
	.loc 1 307 13 is_stmt 1 view .LVU97
	.loc 1 307 26 is_stmt 0 view .LVU98
	movs	r3, #11
	strb	r3, [r0, #267]
	.loc 1 308 13 is_stmt 1 view .LVU99
	.loc 1 308 18 is_stmt 0 view .LVU100
	ldr	r3, [r0, #12]
	.loc 1 308 13 view .LVU101
	mov	r0, sp
.LVL23:
	.loc 1 308 13 view .LVU102
	blx	r3
.LVL24:
	.loc 1 314 13 is_stmt 1 view .LVU103
.LBE30:
	.loc 1 295 14 is_stmt 0 view .LVU104
	movs	r0, #0
.LVL25:
.L14:
	.loc 1 363 1 view .LVU105
	add	sp, sp, #36
.LCFI12:
	@ sp needed
	pop	{r4, r5, pc}
.LVL26:
.L18:
.LCFI13:
.LBB31:
	.loc 1 318 13 is_stmt 1 view .LVU106
	.loc 1 318 54 is_stmt 0 view .LVU107
	add	r5, r0, #197
	.loc 1 318 13 view .LVU108
	mov	r1, r5
	bl	prov_utils_generate_oob_data
.LVL27:
	.loc 1 320 13 is_stmt 1 view .LVU109
	.loc 1 321 13 view .LVU110
	.loc 1 321 24 is_stmt 0 view .LVU111
	movs	r3, #5
	strb	r3, [sp]
	.loc 1 322 13 is_stmt 1 view .LVU112
	.loc 1 322 51 is_stmt 0 view .LVU113
	str	r4, [sp, #4]
	.loc 1 323 13 is_stmt 1 view .LVU114
	.loc 1 323 53 is_stmt 0 view .LVU115
	ldrb	r3, [r4, #262]	@ zero_extendqisi2
	.loc 1 323 46 view .LVU116
	strb	r3, [sp, #9]
	.loc 1 324 13 is_stmt 1 view .LVU117
	.loc 1 324 55 is_stmt 0 view .LVU118
	ldrb	r3, [r4, #263]	@ zero_extendqisi2
	.loc 1 324 48 view .LVU119
	strb	r3, [sp, #8]
	.loc 1 325 13 is_stmt 1 view .LVU120
	.loc 1 325 48 is_stmt 0 view .LVU121
	str	r5, [sp, #12]
	.loc 1 326 13 is_stmt 1 view .LVU122
	.loc 1 326 26 is_stmt 0 view .LVU123
	movs	r3, #15
	strb	r3, [r4, #267]
	.loc 1 327 13 is_stmt 1 view .LVU124
	.loc 1 327 18 is_stmt 0 view .LVU125
	ldr	r3, [r4, #12]
	.loc 1 327 13 view .LVU126
	mov	r0, sp
	blx	r3
.LVL28:
	.loc 1 333 13 is_stmt 1 view .LVU127
.LBE31:
	.loc 1 295 14 is_stmt 0 view .LVU128
	movs	r0, #0
	b	.L14
.LVL29:
.L19:
.LBB32:
	.loc 1 338 13 is_stmt 1 view .LVU129
	.loc 1 339 13 view .LVU130
	.loc 1 339 24 is_stmt 0 view .LVU131
	movs	r3, #7
	strb	r3, [sp]
	.loc 1 340 13 is_stmt 1 view .LVU132
	.loc 1 340 51 is_stmt 0 view .LVU133
	str	r0, [sp, #4]
	.loc 1 341 13 is_stmt 1 view .LVU134
	.loc 1 341 26 is_stmt 0 view .LVU135
	movs	r3, #12
	strb	r3, [r0, #267]
	.loc 1 342 13 is_stmt 1 view .LVU136
	.loc 1 342 18 is_stmt 0 view .LVU137
	ldr	r3, [r0, #12]
	.loc 1 342 13 view .LVU138
	mov	r0, sp
.LVL30:
	.loc 1 342 13 view .LVU139
	blx	r3
.LVL31:
	.loc 1 348 13 is_stmt 1 view .LVU140
.LBE32:
	.loc 1 295 14 is_stmt 0 view .LVU141
	movs	r0, #0
	b	.L14
.LVL32:
.L20:
	.loc 1 351 13 is_stmt 1 view .LVU142
	movs	r0, #0
.LVL33:
	.loc 1 351 13 is_stmt 0 view .LVU143
	str	r0, [r4, #197]	@ unaligned
	str	r0, [r4, #201]	@ unaligned
	str	r0, [r4, #205]	@ unaligned
	str	r0, [r4, #209]	@ unaligned
	.loc 1 352 13 is_stmt 1 view .LVU144
	.loc 1 352 26 is_stmt 0 view .LVU145
	movs	r3, #15
	strb	r3, [r4, #267]
	.loc 1 353 13 is_stmt 1 view .LVU146
	b	.L14
.LVL34:
.L21:
	.loc 1 298 5 is_stmt 0 view .LVU147
	movs	r0, #3
.LVL35:
	.loc 1 362 5 is_stmt 1 view .LVU148
	.loc 1 362 12 is_stmt 0 view .LVU149
	b	.L14
.LFE429:
	.size	request_authentication, .-request_authentication
	.section	.text.send_failed,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.type	send_failed, %function
send_failed:
.LVL36:
.LFB425:
	.loc 1 77 1 is_stmt 1 view -0
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 1 77 1 is_stmt 0 view .LVU151
	push	{r4, r5, lr}
.LCFI14:
	sub	sp, sp, #36
.LCFI15:
	mov	r4, r0
	mov	r5, r1
	.loc 1 78 5 is_stmt 1 view .LVU152
	.loc 1 78 24 is_stmt 0 view .LVU153
	ldr	r0, [r0, #8]
.LVL37:
	.loc 1 78 24 view .LVU154
	bl	prov_tx_failed
.LVL38:
	.loc 1 78 8 view .LVU155
	cbz	r0, .L24
	.loc 1 80 9 is_stmt 1 view .LVU156
	.loc 1 80 14 is_stmt 0 view .LVU157
	ldr	r0, [r4, #8]
	.loc 1 80 31 view .LVU158
	ldr	r3, [r0, #8]
	.loc 1 80 44 view .LVU159
	ldr	r3, [r3, #16]
	.loc 1 80 9 view .LVU160
	movs	r1, #2
	blx	r3
.LVL39:
.L24:
	.loc 1 85 5 is_stmt 1 view .LVU161
	.loc 1 85 14 is_stmt 0 view .LVU162
	ldrb	r3, [r4, #267]	@ zero_extendqisi2
	.loc 1 85 8 view .LVU163
	cmp	r3, #21
	beq	.L23
.LBB33:
	.loc 1 87 9 is_stmt 1 view .LVU164
	.loc 1 88 9 view .LVU165
	.loc 1 88 24 is_stmt 0 view .LVU166
	movs	r3, #12
	strb	r3, [sp]
	.loc 1 89 9 is_stmt 1 view .LVU167
	.loc 1 89 43 is_stmt 0 view .LVU168
	str	r4, [sp, #4]
	.loc 1 90 9 is_stmt 1 view .LVU169
	.loc 1 90 46 is_stmt 0 view .LVU170
	strb	r5, [sp, #8]
	.loc 1 95 9 is_stmt 1 view .LVU171
	.loc 1 95 29 is_stmt 0 view .LVU172
	strb	r5, [r4, #266]
	.loc 1 96 9 is_stmt 1 view .LVU173
	.loc 1 96 22 is_stmt 0 view .LVU174
	movs	r3, #21
	strb	r3, [r4, #267]
	.loc 1 98 9 is_stmt 1 view .LVU175
	.loc 1 98 14 is_stmt 0 view .LVU176
	ldr	r3, [r4, #12]
	.loc 1 98 9 view .LVU177
	mov	r0, sp
	blx	r3
.LVL40:
.L23:
.LBE33:
	.loc 1 100 1 view .LVU178
	add	sp, sp, #36
.LCFI16:
	@ sp needed
	pop	{r4, r5, pc}
	.loc 1 100 1 view .LVU179
.LFE425:
	.size	send_failed, .-send_failed
	.section	.text.start_authentication,"ax",%progbits
	.align	1
	.syntax unified
	.thumb
	.thumb_func
	.type	start_authentication, %function
start_authentication:
.LVL41:
.LFB430:
	.loc 1 366 1 is_stmt 1 view -0
	@ args = 0, pretend = 0, frame = 32
	@ frame_needed = 0, uses_anonymous_args = 0
	.loc 1 366 1 is_stmt 0 view .LVU181
	push	{r4, lr}
.LCFI17:
	sub	sp, sp, #32
.LCFI18:
	mov	r4, r0
	.loc 1 367 5 is_stmt 1 view .LVU182
	.loc 1 367 9 is_stmt 0 view .LVU183
	bl	prov_utils_use_ecdh_offloading
.LVL42:
	.loc 1 367 8 view .LVU184
	cbz	r0, .L28
.LBB34:
	.loc 1 369 9 is_stmt 1 view .LVU185
	.loc 1 370 9 view .LVU18