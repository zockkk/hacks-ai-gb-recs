import {ButtonHTMLAttributes, DetailedHTMLProps, ReactNode} from "react";

interface Props extends DetailedHTMLProps<ButtonHTMLAttributes<HTMLButtonElement>, HTMLButtonElement> {
  children: ReactNode;
}

export function Button(props: Props) {
  const {children, type, ...restProps} = props;
  return (
    <button
      className="bg-gray-50 hover:bg-gray-200 text-sm font-semibold text-gray-800 py-2 px-4 border border-gray-400 rounded shadow"
      type={type || "button"}
      {...restProps}
    >
      {children}
    </button>
  )
}