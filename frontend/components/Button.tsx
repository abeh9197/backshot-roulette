'use client';

type ButtonProps = {
    label: string;
    onClick: () => void;
};

export default function Button( { label, onClick }: ButtonProps) {
    return (
        <button
            className="bg-primary text-white font-bold py-2 px-4 rounded hover:bg-secondary"
            onClick={onClick}
        >
            {label}
        </button>
    );
}