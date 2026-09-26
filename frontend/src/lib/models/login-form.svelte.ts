import { getToken } from '$lib/apis/auth';
import { authStore } from '$lib/stores/auth-store.svelte';
import type { LoginDetails, TokenResponse } from '$lib/types/auth';
import { BaseForm } from './base-form.svelte';

export class LoginForm extends BaseForm<LoginDetails, TokenResponse> {
	email = $state('');
	passowrd = $state('');

	isValid = $derived(this.email.trim().length > 0 && this.passowrd.trim().length > 0);

	async executeSubmit(): Promise<TokenResponse> {
		const result = await getToken(this.email, this.passowrd);
		authStore.login(result.access_token);
		return result;
	}
}
