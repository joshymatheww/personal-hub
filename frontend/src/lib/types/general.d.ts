export type ToastType = 'success' | 'error';
export interface IToast {
	id: string;
	title: string;
	content: string;
	type: ToastType;
}
