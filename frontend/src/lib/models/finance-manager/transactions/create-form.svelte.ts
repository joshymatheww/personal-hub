import { postResource } from '$lib/apis/http';
import { BaseForm } from '$lib/models/base-form.svelte';
import type {
	PaymentMode,
	Transaction,
	TransactionBase,
	TransactionType
} from '$lib/types/finance';
import { format } from 'date-fns';

export class TransactionCreateForm extends BaseForm<TransactionBase, Transaction> {
	type = $state<TransactionType>('expense');
	title = $state('');
	amount = $state('');
	accountId = $state('');
	toAccount = $state<string | null>('');
	category = $state('');
	paymentMode = $state<PaymentMode>('cash');
	vendor = $state('');
	description = $state('');
	groupId = $state<string | null>(null);
	transactionTime = $state(format(new Date(), "yyyy-MM-dd'T'HH:mm"));

	async executeSubmit(token: string): Promise<Transaction> {
		const newTransaction: TransactionBase = {
			account_id: this.accountId ? Number(this.accountId) : -1,
			amount: Number(this.amount),
			description: this.description,
			payment_mode: this.paymentMode,
			title: this.title,
			transaction_time: new Date(this.transactionTime),
			type: this.type,
			group_id: this.groupId ? Number(this.groupId) : undefined,
			to_account: this.toAccount ? Number(this.toAccount) : undefined,
			vendor: this.vendor,
			category: this.category
		};
		const result = await postResource<TransactionBase, Transaction>(
			newTransaction,
			token,
			'finance/transactions'
		);
		return result;
	}

	resetForm() {
		this.type = 'expense';
		this.title = '';
		this.amount = '';
		this.accountId = '';
		this.toAccount = null;
		this.category = '';
		this.paymentMode = 'cash';
		this.vendor = '';
		this.description = '';
		this.groupId = null;
		this.transactionTime = format(new Date(), "yyyy-MM-dd'T'HH:mm");
	}
}
