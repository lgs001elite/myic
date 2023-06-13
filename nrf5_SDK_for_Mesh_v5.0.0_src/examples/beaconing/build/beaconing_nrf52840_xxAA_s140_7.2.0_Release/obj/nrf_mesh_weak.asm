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
	.file	"nrf_mesh_weak.c"
	.text
	.section	.text._weak_handler,"ax",%progbits
	.align	1
	.global	_weak_handler
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	_weak_handler, %function
_weak_handler:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	movs	r0, #6
	bx	lr
	.size	_weak_handler, .-_weak_handler
	.weak	mesh_flash_init
	.thumb_set mesh_flash_init,_weak_handler
	.weak	mesh_flash_op_execute
	.thumb_set mesh_flash_op_execute,_weak_handler
	.weak	nrf_mesh_dfu_state_get
	.thumb_set nrf_mesh_dfu_state_get,_weak_handler
	.weak	nrf_mesh_dfu_rx
	.thumb_set nrf_mesh_dfu_rx,_weak_handler
	.weak	nrf_mesh_dfu_request
	.thumb_set nrf_mesh_dfu_request,_weak_handler
	.weak	nrf_mesh_dfu_relay
	.thumb_set nrf_mesh_dfu_relay,_weak_handler
	.weak	nrf_mesh_dfu_jump_to_bootloader
	.thumb_set nrf_mesh_dfu_jump_to_bootloader,_weak_handler
	.weak	nrf_mesh_dfu_bank_info_get
	.thumb_set nrf_mesh_dfu_bank_info_get,_weak_handler
	.weak	nrf_mesh_dfu_bank_flash
	.thumb_set nrf_mesh_dfu_bank_flash,_weak_handler
	.weak	nrf_mesh_dfu_abort
	.thumb_set nrf_mesh_dfu_abort,_weak_handler
	.weak	nrf_mesh_dfu_enable
	.thumb_set nrf_mesh_dfu_enable,_weak_handler
	.weak	nrf_mesh_dfu_init
	.thumb_set nrf_mesh_dfu_init,_weak_handler
	.weak	prov_utils_opt_get
	.thumb_set prov_utils_opt_get,_weak_handler
	.weak	prov_utils_opt_set
	.thumb_set prov_utils_opt_set,_weak_handler
	.weak	prov_bearer_adv_packet_in
	.thumb_set prov_bearer_adv_packet_in,_weak_handler
	.weak	prov_beacon_unprov_packet_in
	.thumb_set prov_beacon_unprov_packet_in,_weak_handler
	.weak	prov_provisionee_shared_secret
	.thumb_set prov_provisionee_shared_secret,_weak_handler
	.weak	prov_provisionee_auth_data
	.thumb_set prov_provisionee_auth_data,_weak_handler
	.weak	prov_provisionee_listen
	.thumb_set prov_provisionee_listen,_weak_handler
	.weak	prov_provisionee_init
	.thumb_set prov_provisionee_init,_weak_handler
	.weak	prov_provisioner_oob_pubkey
	.thumb_set prov_provisioner_oob_pubkey,_weak_handler
	.weak	prov_provisioner_shared_secret
	.thumb_set prov_provisioner_shared_secret,_weak_handler
	.weak	prov_provisioner_auth_data
	.thumb_set prov_provisioner_auth_data,_weak_handler
	.weak	prov_provisioner_oob_use
	.thumb_set prov_provisioner_oob_use,_weak_handler
	.weak	prov_provisioner_provision
	.thumb_set prov_provisioner_provision,_weak_handler
	.section	.text._weak_handler_ptr,"ax",%progbits
	.align	1
	.global	_weak_handler_ptr
	.syntax unified
	.thumb
	.thumb_func
	.fpu fpv4-sp-d16
	.type	_weak_handler_ptr, %function
_weak_handler_ptr:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	movs	r0, #0
	bx	lr
	.size	_weak_handler_ptr, .-_weak_handler_ptr
	.ident	"GCC: (based on arm-10.3-2021.07 GCC) 10.3.1 20210621 (release)"
