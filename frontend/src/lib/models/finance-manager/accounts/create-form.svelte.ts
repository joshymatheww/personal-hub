import { postResource } from '$lib/apis/http';
import type { AccountBase, Account } from '$lib/types/finance';
import { BaseForm } from '$lib/models/base-form.svelte';

export class AccountForm extends BaseForm<AccountBase, Account> {
	name = $state('');
	balance = $state(0);
	type = $state('');

	async executeSubmit(token: string): Promise<Account> {
		const newExericse: AccountBase = {
			name: this.name,
			balance: this.balance,
			type: this.type
		};
		const result = await postResource<AccountBase, Account>(newExericse, token, 'finance/accounts');
		return result;
	}

	resetForm() {
		this.name = '';
		this.balance = 0;
		this.type = '';
	}
}
