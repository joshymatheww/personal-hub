export type AccountTypes = string[];
export type PaymentModes = string[];
export type TransactionTypes = string[];
export interface Categories {
	income: string[];
	expense: string[];
	transfer: string[];
}

export interface FinanceMeataData {
	account_types: AccountTypes;
	payment_modes: PaymentModes;
	transaction_types: TransactionTypes;
	categories: Categories;
}

export interface AccountBase {
	name: string;
	type: string;
	balance: number;
}

export interface Account extends AccountBase {
	id: number;
}

export interface AccountUpdate {
	name?: string;
	type?: string;
	balance?: number;
}

export interface TransactionGroupBase {
	name: string;
	description?: string;
}

export interface TransactionGroup extends TransactionGroupBase {
	id: number;
}

export interface TransactionGroupUpdate {
	name?: string;
	description?: string;
}

export type TransactionType = 'income' | 'expense' | 'transfer';
export type PaymentMode = 'cash' | 'upi' | 'net_banking' | 'credit_card_direct';

export interface TransactionBase {
	account_id: number;
	to_account?: number;
	group_id?: number;
	title: string;
	transaction_time: Date;
	amount: number;
	type: TransactionType;
	payment_mode: PaymentMode;
	description: string;
	vendor?: string;
	category: string;
}

export interface Transaction extends TransactionBase {
	id: number;
}
