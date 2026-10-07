import { updateResource } from '$lib/apis/http';
import type { Account, AccountUpdate } from '$lib/types/finance';
import { BaseForm } from '$lib/models/base-form.svelte';

export class AccountUpdateForm extends BaseForm<AccountUpdate, Account> {
	name = $state('');
	balance = $state(0);
	type = $state('');
	id = $state(0);

	constructor(account: Account) {
		super();
		this.name = account.name;
		this.balance = account.balance;
		this.type = account.type;
		this.id = account.id;
	}

	async executeSubmit(token: string): Promise<Account> {
		const updateData: AccountUpdate = {
			name: this.name,
			balance: this.balance,
			type: this.type
		};
		const result = await updateResource<AccountUpdate, Account>(
			updateData,
			token,
			`finance/accounts/${this.id}`
		);
		return result;
	}
}
